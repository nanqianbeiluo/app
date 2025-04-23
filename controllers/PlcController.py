from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus import ModbusException
import time
from controllers.action_mappings import ACTION_MAPPING, ACTION_GROUPS
from controllers.alarm_code import ALARM_CODE
import logging
import re
from colorlog import ColoredFormatter

class NoColorFileFormatter(logging.Formatter):
    """用于文件日志的格式化器（去除ANSI颜色代码）"""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    def format(self, record):
        message = super().format(record)
        return self.ansi_escape.sub('', message)

class ColorConsoleFormatter(ColoredFormatter):
    """用于控制台的彩色格式化器"""
    def __init__(self):
        super().__init__(
            "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            reset=True,
            log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red,bg_white'
            }
        )

class PlcController:
    def __init__(self, host, port=502):
        self._monitor_running = False
        self.host = host
        self.port = port
        self.client = ModbusClient(self.host)
        self.monitor_running = False
        self.action_mapping = ACTION_MAPPING
        self._configure_logging()  # 初始化日志配置
        self.connect()

    def _configure_logging(self):
        """自定义日志配置方法"""
        self.logger = logging.getLogger('PLCController')
        self.logger.setLevel(logging.DEBUG)

        # 清除已有处理器
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        # 控制台处理器（带颜色）
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(ColorConsoleFormatter())  # 使用彩色格式化

        # 文件处理器（无颜色）
        file_handler = logging.FileHandler('plc_operations.log')
        file_handler.setFormatter(NoColorFileFormatter(  # 使用去色格式化
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt="%Y-%m-%d %H:%M:%S"
        ))

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def connect(self):
        # self.client = ModbusClient(self.host, port=self.port)
        # if not self.client.connect():
        #     self.logger.error(f"连接失败 | Host: {self.host}:{self.port}")  # 错误日志
        #     raise ConnectionError("无法连接到Modbus服务器")
        # self.logger.info(f"成功建立连接 | Host: {self.host}:{self.port}")
        if not self.client.is_socket_open():
            self.client.connect()
        if self.client.is_socket_open():
            self.logger.info(f"成功建立连接 Host: {self.host}:{self.port}")
        else:
            self.logger.error(f"连接失败 Host: {self.host}:{self.port}")
            raise ConnectionError("无法连接到Modbus服务器")

    def disconnect(self):
        # if self.client:
        #     self.client.close()
        #     self.logger.info("连接已正常关闭")  # 关闭日志
        if self.client and self.client.is_socket_open():
            self.client.close()
            self.logger.info("连接已正常关闭")

    def write_register(self, address, value):
        self.logger.debug(f"开始写入参数，地址={address}, 值={value}")

        # 获取寄存器地址和值
        register_address = address
        register_value = value

        try:
            # 尝试写入寄存器
            result = self.client.write_register(register_address, register_value)
            if result:
                self.logger.debug(f"写入寄存器成功 | Address: {register_address} | Value: {register_value}")
            else:
                self.logger.error(f"写入寄存器失败 | Address: {register_address} | Value: {register_value}")
            return result
        except Exception as e:
            self.logger.error(
                f"写入寄存器时发生异常 | Address: {register_address} | Value: {register_value} | 错误: {str(e)}")
            return False

    def read_register(self, address):
        """读取指定寄存器的值"""
        try:
            response = self.client.read_holding_registers(address,count=1)
            if not response.isError():
                return response.registers
            else:
                raise ModbusException(f"读取寄存器失败: {response.exception()}")
        except ModbusException as e:
            self.logger.error(f"读取寄存器异常 | Address: {address} | Error: {str(e)}")
            return None

    def check_alarms(self):
        """
        检查报警代码并进行急停。
        :return: 报警代码或None。
        """
        alarm_address = 704
        emergency_stop_address = 615  # 急停寄存器地址
        emergency_stop_value = 1  # 急停值
        self.connect()
        try:
            alarm_code = self.client.read_holding_registers(alarm_address).registers[0]
            if alarm_code != 0:
                # 执行急停操作
                self.client.write_register(emergency_stop_address, emergency_stop_value)
                alarm_message = ALARM_CODE.get(alarm_code, "未知报警")
                self.logger.warning(f"检测到报警：代码 {alarm_code}, 内容 {alarm_message}")
                return alarm_code, alarm_message
            return None
        except ModbusException as e:
            self.logger.error(f"读取报警代码时发生Modbus异常: {e}")
            return None
        except Exception as e:
            self.logger.error(f"读取报警代码时发生异常: {e}")
            return None

    def execute_action(self, action, timeout=300):
        if self.check_alarms() is not None:
            return "Error: 检测到报警，执行急停"

        try:
            action_details = self.action_mapping.get(action)
            if not action_details:
                self.logger.error(f"无效动作名称: {action}")  # 错误日志
                return "Error: 动作映射不存在"

            # 处理一对一和多对一的情况
            if isinstance(action_details, dict):
                action_details = [action_details]

            # 发送plc指令
            for details in action_details:
                self.client.write_register(details['write_address'], details['command_value'])
                self.logger.debug(  f"写入寄存器 | Address: {details['write_address']} "f"Value: {details['command_value']}")# 详细操作日志

            start_time = time.time()
            while True:
                # 等待一段时间让PLC处理指令
                time.sleep(2)
                # 检查状态
                status_report = []
                all_completed = True
                for details in action_details:
                    status = self.client.read_holding_registers(details['status_address']).registers[0]
                    # status = self.client.read_holding_registers(details['status_address'], 1).registers[0]
                    status_report.append(f"{details['status_address']}={status}(期望:{details['command_value']})")
                    if status != details['command_value']:
                        all_completed = False
                        break

                self.logger.debug(f"状态检查 | Action: {action} | 状态: {', '.join(status_report)}")# 详细状态日志

                # if all_completed:
                #     # 清除所有指令
                #     for details in action_details:
                #         self.client.write_register(details['write_address'], 0)
                #     return "动作完成"
                if all_completed:
                    for details in action_details:
                    # 判断写入地址是否为600
                        if details['write_address'] == 600:
                            # 清除所有指令
                            self.client.write_register(details['write_address'], 0)
                            self.logger.debug(f"复位寄存器 | Address: {details['write_address']}")
                        self.logger.info(f"动作完成 | Action: {action}")  # 成功日志
                        return "动作完成"

                # 检查是否超时
                if time.time() - start_time > timeout:
                    # 清除所有指令
                    for details in action_details:
                        self.client.write_register(details['write_address'], 0)
                    return "Error: 操作超时"

        except ModbusException as e:
            return f"Modbus异常: {e}"
        except Exception as e:
            return f"异常: {e}"

    def execute_multiple_actions(self, actions, timeout=600):
        try:
            for action in actions:
                result = self.execute_action(action, timeout)
                if "Error" in result:
                    # 如果发生错误，停止执行并返回错误信息
                    return result
            return "所有动作执行完成"
        except Exception as e:
            return f"执行多个动作时发生异常: {e}"

    def execute_action_group(self, action_group_name, timeout=6000):
        """
        执行一个预定义的动作组。
        :param action_group_name: 动作组的名称
        :param timeout: 执行动作组的超时时间
        :return: 执行结果
        """
        self.logger.info(f"开始执行动作组 | Group: {action_group_name}")  # 开始日志

        if not self.client:
            self.connect()
        if not self.client.is_socket_open():
            self.client.connect()
        if not self.client.is_socket_open():
            self.logger.error("PLC连接不可用")  # 错误日志
            return "Error: 无法连接到PLC"

        if action_group_name not in ACTION_GROUPS:
            self.logger.error(f"无效动作组: {action_group_name}")  # 错误日志
            return f"Error: 动作组 '{action_group_name}' 不存在"

        actions = ACTION_GROUPS[action_group_name]
        result = self.execute_multiple_actions(actions, timeout)

        self.logger.info(f"动作组执行完成 | Group: {action_group_name} | Result: {result}")  # 结果日志
        return result

    def get_operate_status(self):
        """
        获取操作状态。
        :return: 状态字符串 ('idle', 'busy', 'finish')
        """
        self.logger.debug("开始查询系统状态")  # 调试日志

        try:
            operate_status_address1 = 600
            operate_status_address2 = 700

            # 读取订单状态和操作状态寄存器
            operate_status_address1 = self.client.read_holding_registers(operate_status_address1).registers[0]
            operate_status_address2 = self.client.read_holding_registers(operate_status_address2).registers[0]

            self.logger.debug(  f"状态查询结果 | 600={operate_status_address1} 700={operate_status_address2}")# 详细状态日志

            # 根据规则判断状态
            if operate_status_address1 == operate_status_address2 == 0:
                return 'idle'
            elif operate_status_address1 != 0:
                return 'busy'
            elif operate_status_address1 == operate_status_address1 and operate_status_address2 != 0:
                return 'finish'
            else:
                return 'failed'
        except ModbusException as e:
            return f"Modbus异常: {e}"
        except Exception as e:
            self.logger.error(f"状态查询失败: {str(e)}", exc_info=True)
            return f"异常: {e}"

    def get_HeaterTem_status(self):
        self.logger.debug("开始查询加热器温度")  # 调试日志

        temperature_status_address = 743
        temperature_set_address    = 631
        result = self.compare_register_values(temperature_status_address, temperature_set_address)

        return result


    def compare_register_values(self, status_address, set_address):
        """
        比较两个Modbus寄存器的值并返回设备状态。

        参数:
            status_address (int): 状态寄存器的地址。
            set_address (int): 设置寄存器的地址。

        返回:
            str: 设备状态，可能的值包括 'no match', 'ready', 'no set', 'failed' 或错误信息。
        """
        self.logger.debug(f"开始查询设备状态，状态地址={status_address}, 设置地址={set_address}")

        try:
            status_response = self.client.read_holding_registers(status_address, count=1)
            set_response = self.client.read_holding_registers(set_address, count=1)

            if not status_response.isError() and not set_response.isError():
                status_value = status_response.registers[0]
                set_value = set_response.registers[0]

                self.logger.debug(f"状态查询结果 | 设置地址={set_value} 状态地址={status_value}")

                if status_value != set_value and set_value != 0:
                    return 'no match'
                elif status_value == set_value and set_value != 0:
                    return 'ready'
                elif status_value == set_value == 0:
                    return 'no set'
                else:
                    return 'failed'
            else:
                status_error = status_response.exception() if status_response.isError() else None
                set_error = set_response.exception() if set_response.isError() else None
                raise ModbusException(
                    f"读取寄存器失败，状态地址={status_address}: {status_error}, 设置地址={set_address}: {set_error}")
        except ModbusException as e:
            return f"Modbus异常: {e}"
        except Exception as e:
            self.logger.error(f"状态查询失败: {str(e)}", exc_info=True)
            return f"异常: {e}"

    def monitor_registers(self, addresses, interval=2, callback=None):
        """
        实时监控指定寄存器
        :param addresses: 要监控的寄存器地址列表（如 [600, 700]）
        :param interval: 轮询间隔（秒）
        :param callback: 数据回调函数（参数为字典，格式 {address: value}）
        """
        import threading
        self._monitor_running = True

        def monitoring_thread():
            while self._monitor_running:
                data = {}
                for addr in addresses:
                    value = self.read_register(addr)
                    if value is not None:
                        data[addr] = value[0]
                if callback:
                    callback(data)
                time.sleep(interval)

        thread = threading.Thread(target=monitoring_thread)
        thread.daemon = True
        thread.start()
        return thread

    def stop_monitoring(self):
        """停止监控"""
        self._monitor_running = False

    def __del__(self):
        self.disconnect()  # 在对象销毁时关闭连接

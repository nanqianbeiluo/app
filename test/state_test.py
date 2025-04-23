'''
Author: Mr_Yao 2316718372@qq.com
Date: 2025-04-18 19:28:40
LastEditors: Mr_Yao 2316718372@qq.com
LastEditTime: 2025-04-18 21:01:41
FilePath: /py_device_test_backend/test/status_test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 此函数无法直接运行请在service中执行

from utils.state import equ_manager
from utils import equ_logger

# 操作功能使用
# 仅设置设备状态

# status为状态 可选择 idle busy failed
# message为设备信息 设计者考虑只有发生故障或者警报时给出提示性信息
# fault_code为故障码 详细故障码请参考故障码表 1101表示数据校验失败
equ_manager.set_equ_status(status="failed", message="设备的一条信息", fault_code="1101")

# 技能中使用
# 技能中不仅要改变设备的状态，还要进行任务状态信息的改变

# 在技能执行反馈信息中插入一条执行信息，一般在技能状态设置前更新
equ_logger.info('一条节点普通的执行信息')
equ_logger.warning('一条节点告警执行信息')
equ_logger.debug('一条节点审查执行信息')
equ_logger.critical('一条节点关键执行信息')
equ_logger.error('一条节点错误执行信息')

# 设备状态和任务状态更新

# 设置设备状态为idle 并更新任务状态为success 表示执行成功
equ_manager.success()
# 设置设备状态为failed 并更新任务状态为failed 表示执行失败
equ_manager.failed()
# failed中还支持code故障码参数的传入
equ_manager.failed(code="1101")
# 设置设备状态为default 并更新任务状态为default 表示未开始执行
equ_manager.default()
# 设置设备状态为default 并更新任务状态为default 表示不需要执行立即跳过
equ_manager.pass_()

# 每一项状态的设置都支持自定义消息的写入 detail默认为第一个参数
equ_manager.success('执行成功！！')


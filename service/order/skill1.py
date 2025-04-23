"""
Author: Mr_Yao 2316718372@qq.com
Date: 2025-04-15 16:03:40
LastEditors: Mr_Yao 2316718372@qq.com
LastEditTime: 2025-04-18 22:24:19
FilePath: /py_mock/service/skill1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
"""
import time
from utils.state import equ_manager
from utils.validate import v_params
from utils import equ_logger

# 必须进行技能定义可为空
REMARK = "一个定时器延迟程序"

# 必须进行参数定义
PARAMS_DEFINITION = {
    "time": {"type": int, "description": "模拟技能执行的时间（秒）。必须是整数。","min":3,"max":8,"mock":5},
    # "dict": {"type": dict, "description": "字典数据"},
    # "list": {"type": list, "description": "列表数据"},
    # "bool": {"type": bool, "description": "布尔值"},
    # "float": {"type": float, "description": "浮点数"},
    # "str": {"type": str, "description": "字符串"}
}
# 必须声明main函数
def main(params: dict) -> None:
    try:    
        # 验证参数
        v_params(params,PARAMS_DEFINITION)

    except ValueError as e:
        # 如果参数校验失败，打印错误信息并停止执行
        equ_manager.failed(detail=f"Parameter validation failed: {e}",code='1101')
        print(f"Parameter validation failed: {e}")
        return  # 或者使用 sys.exit(1) 来直接退出程序

    # 如果参数校验通过，继续执行主程序逻辑
    # 模拟技能执行指定时间
    # equ_logger.info('一条节点执行信息')
    # equ_logger.warning('一条节点执行信息')
    # equ_logger.debug('一条节点执行信息')
    # equ_logger.critical('一条节点执行信息')
    # equ_logger.error('一条节点执行信息')
    # equ_logger.info('一条节点执行信息')

    print(params)

    # 执行循环
    for i in range(params['time']):
        equ_logger.warning(f"正在执行消息 {i + 1}/{params['time']}...")
        time.sleep(1)  # 每条消息间隔 1 秒

    # 技能执行成功后调用此函数
    # equ_manager.success()

    # 设置结果的返回
    equ_manager.success(result=True,detail=f"定时{params['time']}秒任务已完成")

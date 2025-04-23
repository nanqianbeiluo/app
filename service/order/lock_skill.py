'''
Author: Mr_Yao 2316718372@qq.com
Date: 2025-04-15 16:03:40
LastEditors: Mr_Yao 2316718372@qq.com
LastEditTime: 2025-04-17 20:35:03
FilePath: /py_mock/service/skill1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import time
from utils.state import equ_manager
from utils.validate import v_params
from utils import equ_logger

# 必须进行技能定义可为空
REMARK="一个带钥匙的技能"

# 必须进行参数定义
PARAMS_DEFINITION = {
        "lock_key":{"type":str,"description":"钥匙，需要和设备参数中lock_key一致","mock":"lock1"},
        "lock":{"type":str,"description":"新的锁将会一直占用设备，为空时表示不加锁,也就是释放设备","mock":"lock1"},
}
# 必须声明main函数
def main(params: dict) -> None:

    try:    
         # 验证参数
        v_params(params,PARAMS_DEFINITION)
    except ValueError as e:
        # 如果参数校验失败，打印错误信息并停止执行
        equ_manager.failed(f"Parameter validation failed: {e}")
        print(f"Parameter validation failed: {e}")
        return  # 或者使用 sys.exit(1) 来直接退出程序

    # 如果参数校验通过，继续执行主程序逻辑
    # 模拟技能执行指定时间
    time.sleep(2)

    # 技能执行成功后调用此函数
    equ_manager.success()
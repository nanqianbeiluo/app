"""
Author: Mr_Yao 2316718372@qq.com
Date: 2025-04-15 18:38:54
LastEditors: Mr_Yao 2316718372@qq.com
LastEditTime: 2025-04-17 16:18:55
FilePath: /py_mock/service/operate/reset.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
"""
from utils.params import equ_params
from utils.validate import v_params
from utils.state import equ_manager

# 必须进行函数定义可为空
REMARK = "程序清除锁操作"

# 必须声明参数定义
PARAMS_DEFINITION = {}

# 必须声明主函数
def main(params):
    try:    
        # 验证参数
        v_params(params,PARAMS_DEFINITION)
    except ValueError as e:
        # 如果参数校验失败，打印错误信息并停止执行
        print(f"Parameter validation failed: {e}")
        return  # 或者使用 sys.exit(1) 来直接退出程序
    # 打印参数
    # print(f"params: {params}")

    # 调用reset方法软件状态重置
    equ_params.clear_lock()

    # 设置状态为空闲
    equ_manager.set_equ_status(status="idle")

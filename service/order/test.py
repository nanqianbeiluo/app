"""
Author: Li Yuchen
Description: 执行动作组并实时监控参数
"""
# import time
from controllers.PlcController import PlcController
from utils.state import equ_manager
from utils.validate import v_params
import os

# 进行技能定义
REMARK = "测试"

# 参数定义
PARAMS_DEFINITION = {
    "action_group": {"type": str,
                     "description": "这是用于测试的order",
                     "mock": 'test'},
}

def main(params: dict) -> None:
    try:
        # 参数验证
        v_params(params, PARAMS_DEFINITION)

        host = os.getenv('HOST', '192.168.1.101')
        # 初始化PLC控制器
        plc = PlcController(host)  # 替换实际IP

        # 执行动作组
        result = plc.execute_action_group(params['action_group'])

        if "Error" in result:
            equ_manager.failed(detail=result, code="1201")
        else:
            equ_manager.success(result=result, detail="动作组执行完成")

    except ValueError as e:
        equ_manager.failed(detail=f"参数错误: {e}", code="1101")
    except Exception as e:
        equ_manager.failed(detail=f"执行异常: {str(e)}", code="1201")

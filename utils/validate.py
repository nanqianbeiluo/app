'''
Author: Mr_Yao 2316718372@qq.com
Date: 2025-04-16 14:24:18
LastEditors: Mr_Yao 2316718372@qq.com
LastEditTime: 2025-04-16 17:36:53
FilePath: /py_mock/utils/validate_params.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import re

def v_params(params: dict, params_definition: dict) -> None:
    """
    验证参数是否符合指定的定义。

    Args:
        params (dict): 要验证的参数字典。
        params_definition (dict): 参数定义字典，包含字段名称、类型和描述。
            - 键为参数名称。
            - 值为一个字典，包含以下键：
                - 'type': 参数的期望类型。
                - 'description': 参数的描述（可选）。
                - 'min': 最小值（可选，仅对数值类型有效）。
                - 'max': 最大值（可选，仅对数值类型有效）。
                - 'regex': 正则表达式（可选，仅对字符串类型有效）。

    Raises:
        ValueError: 如果参数缺失、类型不匹配或值超出范围。
    """
    for field, field_info in params_definition.items():
        if field not in params:
            raise ValueError(f"params must contain '{field}' field")
        value = params[field]
        expected_type = field_info["type"]

        # 类型检查
        if not isinstance(value, expected_type):
            raise ValueError(f"The value of '{field}' must be of type {expected_type.__name__}, "
                             f"but got {type(value).__name__}")

        # 数值类型范围检查
        if isinstance(value, (int, float)):
            if "min" in field_info and value < field_info["min"]:
                raise ValueError(f"'{field}' should be >= {field_info['min']}")
            if "max" in field_info and value > field_info["max"]:
                raise ValueError(f"'{field}' should be <= {field_info['max']}")

        # 字符串正则校验
        if isinstance(value, str) and "regex" in field_info:
            if not re.match(field_info["regex"], value):
                raise ValueError(f"'{field}' does not match the pattern {field_info['regex']}")
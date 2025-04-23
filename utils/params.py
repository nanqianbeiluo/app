'''
Author: Mr_Yao 2316718372@qq.com
Date: 2025-04-15 17:05:40
LastEditors: Mr_Yao 2316718372@qq.com
LastEditTime: 2025-04-18 15:46:07
FilePath: /py_mock/utils/params.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import time
from typing import Any, Callable, Dict, Union
from datetime import datetime, timezone, timedelta

# 获取当前时间戳
current_timestamp = time.time()

# 转换为北京时间（UTC+8）
beijing_time = datetime.fromtimestamp(current_timestamp, timezone(timedelta(hours=8)))

class Params:
    def __init__(self):
        self.params = {
            "volt": 40,
            # "dict1":{"name":"张三"},
            # "list":[100,200],
            "start_time":beijing_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.params['lock_key'] = None

    def get(self) -> Dict[str, Any]:
        """获取当前参数"""
        return self.params

    def set(self, fn: Callable[[Dict[str, Any]], Dict[str, Any]]) -> None:
        """修改参数"""
        if not callable(fn):
            raise ValueError("fn must be a callable function")
        self.params = fn(self.params)

    def lock(self, lock_key: Any) -> None:
        """上锁"""
        self.params['lock_key'] = lock_key

    def unlock(self, key: str) -> bool:
        """开锁"""
        # 如果 lock_key 是 None 或空字符串，直接返回 True
        if self.params['lock_key'] is None or self.params['lock_key'] == "":
            return True

        return self.params['lock_key'] == key
    
    def clear_lock(self) -> None:
        """开锁"""
        self.params['lock_key'] = None

    def update_path(self, path: str, value: Any) -> None:
        """更新路径"""
        parts = [part for part in path.split("/") if part]  # 分割路径并去除空字符串
        current = self.params  # 从顶层对象开始

        for part in parts[:-1]:
            if part.isdigit():
                index = int(part)
                if index >= len(current):
                    current[index] = {}
                current = current[index]
            else:
                if part not in current:
                    current[part] = {}
                current = current[part]

        last_part = parts[-1]
        if last_part.isdigit():
            current[int(last_part)] = value
        else:
            current[last_part] = value

# 创建一个全局实例
equ_params = Params()
'''
Author: Mr_Yao 2316718372@qq.com
Date: 2025-04-18 15:33:43
LastEditors: Mr_Yao 2316718372@qq.com
LastEditTime: 2025-04-21 09:43:47
FilePath: /py_device_test_backend/test/read_demo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 此函数无法直接运行请在service中执行

from utils.params import equ_params

# 获取设备参数
params=equ_params.get()

print(params)

# 新增或修改参数
params.update_path(path="/test_params",value=1)
# 重新获取设备参数
params=equ_params.get()

print(params)

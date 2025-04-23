'''
Author: Mr_Yao 2316718372@qq.com
Date: 2025-04-17 15:29:06
LastEditors: Mr_Yao 2316718372@qq.com
LastEditTime: 2025-04-17 15:39:42
FilePath: /py_mock/utils/equ_logger.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from utils.state import equ_manager

# 该函数可以往->任务执行反馈信息中添加消息

def debug(detail=None):
    equ_manager.add_detail(detail=detail,level='debug')

def info(detail=None):
    equ_manager.add_detail(detail=detail,level='info')

def warning(detail=None):
    equ_manager.add_detail(detail=detail,level='warning')

def error(detail=None):
    equ_manager.add_detail(detail=detail,level='error')

def critical(detail=None):
    equ_manager.add_detail(detail=detail,level='critical')
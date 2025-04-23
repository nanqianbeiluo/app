'''
Author: Mr_Yao 2316718372@qq.com
Date: 2025-04-18 21:30:16
LastEditors: Mr_Yao 2316718372@qq.com
LastEditTime: 2025-04-18 21:31:13
FilePath: /py_device_test_backend/test/log_test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from utils.logger import logger

logger.info('一条节点执行信息')
logger.warning('一条节点执行信息')
logger.debug('一条节点执行信息')
logger.critical('一条节点执行信息')
logger.error('一条节点执行信息')
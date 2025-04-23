'''
Author: Mr_Yao 2316718372@qq.com
Date: 2025-04-16 19:25:53
LastEditors: Mr_Yao 2316718372@qq.com
LastEditTime: 2025-04-18 19:28:59
FilePath: /py_mock/scheduled/task1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from utils.logger import logger

'''
# CronTrigger 的参数说明：
#   second: 秒（取值范围 0-59)。
#   minute: 分钟（取值范围 0-59)。
#   hour: 小时（取值范围 0-23)。
#   day: 日期（取值范围 1-31)。
#   month: 月份（取值范围 1-12)。
#   day_of_week: 星期几(0-6 或 mon,tue,wed,thu,fri,sat,sun)。
#   start_date: 触发器的最早触发日期/时间。
#   end_date: 触发器的最晚触发日期/时间。
#   timezone: 时区。
'''

# 必须定义此参数
SCHEDULE_CONFIG = {
    "trigger": "cron",
    "second": "*/3"  # 每3秒执行一次
}

# 执行次数
sum = 0

# 必须定义run方法
def run():
    global sum  # 声明使用全局变量sum
    sum += 1  # 修改全局变量sum的值
 
    # print(f"{new_time}: Task 1 is running...{sum}")
    logger.info(f"Task 1 is running...,已累计执行:{sum}次")

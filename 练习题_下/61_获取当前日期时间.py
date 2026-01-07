# 获取并显示当前日期和时间


# ------ 我的答案 ------------------
# import time
# from dateutil import parser
#
# print(time.ctime())
# print(parser.parse(time.ctime()))


# --------参考答案------------
import datetime

current_time = datetime.datetime.now()
print(current_time)

current_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
print(current_str)

year = current_time.year
month = current_time.month
day = current_time.day
hour = current_time.hour
minute = current_time.minute
second = current_time.second
print(f'当前年份：{year}')
print(month)
print(day)
print(hour)
print(minute)
print(second)


# ---------- 总结 ---------
# 1、获取当前的日期及时间：
#   导入日期时间模块 datetime
#   datetime.datetime.now()
#
# 2、日期时间的格式化：
#   日期时间.strftime(格式)
#
# 3、日期时间的年月日时分秒提取

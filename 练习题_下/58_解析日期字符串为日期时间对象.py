# 解析给定的日期字符串"Aug 28 2025 12:00AM" ,并打印出解析后的日期时间对象

from dateutil import parser
import time
import datetime

date_string = "Aug28-2025 12:00AM"
a1 = "2026-01-01 07:51:26"
a2 = '2025/12/30 22:56:24'
a3 = '2026/1/1 08:00:00'
parsed_date = parser.parse(date_string)
print(parsed_date)
print(parser.parse(a1))
print(parser.parse(a2))
# print(parser.parse(time.localtime())) -- 这个是时间数组格式，解析不了
print(parser.parse(time.ctime()))



# -------- 总结 ----------
# 1、dateutil库安装：
# pip install python-dateutil
#
# 2、parser.pase()
# 参数是各种形式的年月日时分秒，都可以解析成 2026-01-01 07:51:26 这种格式
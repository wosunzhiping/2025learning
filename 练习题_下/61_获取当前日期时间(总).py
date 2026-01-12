# 获取并显示当前日期和时间


# ------ 我的答案 ------------------
# import time
# from dateutil import parser
#
# print(time.ctime())
# print(parser.parse(time.ctime()))


# --------参考答案------------
import datetime
import time

current_time = datetime.datetime.now()
print(current_time)
print(type(current_time))

datetime_to_str1 = current_time.strftime('%Y-%m-%d %H:%M:%S')
datetime_to_str2 = datetime.datetime.strftime(current_time,'%Y-%m-%d')



time_to_str1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# c1 = current_time.strf  ---- 没有


print(datetime_to_str1)
print(datetime_to_str2)
print(time_to_str1)


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



current_str2 = datetime.datetime.strftime(current_time,'%Y-%m-%d')
str_now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())


# ---------- 总结 ---------
# 1、获取当前的日期及时间：
#   导入日期时间模块 datetime
#   datetime.datetime.now()，得到的是 datetime 类型对象
#
# 2、日期时间格式化成字符串：以下三种，输出的时间都是string类型
# 1）time.strftime('时间格式',结构化时间对象)
# 2）datetime.datetime.now().strftime('时间格式')
# 3）datetime.datetime.strftime(datetime.datetime对象，'时间格式')
#
#3、时间字符串格式化成指定时间结构类型：
# 1）datetime.datetime.strptime(时间字符串,'前面时间字符串对应的时间格式') 结果是 datetime.datetime 对象
# 2）time.strptime(时间字符串,'前面时间字符串对应的时间格式')) 结果是time_struct 对象
# 3、日期时间的年月日时分秒提取：
# datetime.datetime类型对象.year

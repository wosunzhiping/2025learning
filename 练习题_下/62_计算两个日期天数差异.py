# 计算两个日期之间的天数差异


# -------- 我的答案 ----------------
from datetime import date

start_date = '2025-11-18'
end_date = '2026-05-15'

year1,month1,day1 = map(int,start_date.split('-'))
year2,month2,day2 = map(int,end_date.split('-'))
print(map(int,start_date.split('-')))

d1 = date(year1,month1,day1)
d2 = date(year2,month2,day2)

print(type(d1))

delta = d2 - d1
print(delta)
print(abs(delta.days))


# -------- 参考答案 -------------
# import datetime
#
# start_day = '2025-11-18'
# end_date = datetime.datetime.now()
#
# print(type(end_date))
#
# start_date = datetime.datetime.strptime(start_day,'%Y-%m-%d')
#
# delta = end_date - start_date
#
# print(delta)
# print(delta.days)


# --------- 总结 ----------
# 1、时间字符串转换成datetime类型，然后才可以跟datetime类型的时间相减：
#   datetime.datetime.striptime(时间字符串，时间格式)
#   注意，入参2中的时间格式是入参1本身的时间格式，输出是带有时分秒的datetime格式的时间

# 2、两个datetime格式的时间可以直接相减，计算天数、时间间隔
#
# 3、提取间隔的天数，可以用delta.days属性提取

# 4、year1,month1,day1 = map(int,start_date.split('-'))
# 1）map的解包
# 2）map(int,列表) 输出是一个map对象
#
# 5、date(year1,month1,day1)
# 1）date类型对象的创建，用date(年，月，日)
# 2）date对象直接相减，可以得到两个日期天数及时间之差






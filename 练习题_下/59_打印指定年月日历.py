# 用户输入年份和月份，打印该月份对应的日历

import calendar

year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
print(calendar.month(year,month))
print(type(calendar.month(year,month)))


# ------ 总结 ——————————--
# 1、canlendar.month(年，月) 打印对应的日历
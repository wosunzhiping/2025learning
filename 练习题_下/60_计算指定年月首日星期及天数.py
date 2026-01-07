# 计算并打印指定年月的第一天是星期几，以及该月份的天数

import calendar

year = int(input('请输入年份：'))
month = int(input('请输入月份：'))

# 元组的解包
first_day,days_of_month = calendar.monthrange(year,month)

# 定义一个星期的列表，直接用calendar.monthrange结果的索引来映射中文星期
week_list = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
first_day_week = week_list[first_day]


print(calendar.monthrange(year,month))
print(f'{year}年{month}月的第一天是{first_day_week}，这个月一共有{days_of_month}天')


# --------- 总结 ----------
# 1、calendar.monthragne(年，月)：
#   返回一个元组，(本月第一天是周几的索引，本月一共多少天)
#
# 2、元组的解包：
# a,b = calendar.monthrange(year,month)
#
# 3、定义星期列表，直接用索引映射具体周几

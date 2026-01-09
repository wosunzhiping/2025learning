# 编写一个程序，使用datetime模块完成以下功能：
# 1、输出今日日期，YYYY-MM-DD格式
# 2、创建并输出小红生日--1941年1月5日的日期
# 3、计算并输出其生日的下一天
# 4、计算并输出其一岁生日日期

import datetime

today = datetime.datetime.now().strftime('%Y-%m-%d')
print(today)

birthday_datetime = datetime.datetime.strptime('1941-1-5','%Y-%m-%d')
print(f'生成的生日日期是：{birthday_datetime}')


# ------ 参考答案开始 ---------
birthday = datetime.date(1941,1,5)
print(f'生成的生日日期是：{birthday}')
# ------ 参考答案截止--------

birthday_nextday = birthday_datetime + datetime.timedelta(days=1)
print(birthday_nextday)



birthday_nextyear = birthday_datetime + datetime.timedelta(365)
print(birthday_nextyear)

# ------ 参考答案开始 ---------
birthday_nextday_1 = birthday + datetime.timedelta(days=1)
first_birthday = birthday.replace(year=birthday.year + 1)
print(f'生日的下一天是：{birthday_nextday_1}')
print(f'第一个生日日期是:{first_birthday}')

# ------ 参考答案截止 ---------



# --------总结---------
# 1、日期格式：
# YYYY-MM-DD 格式，写成格式化字符串是 %Y-%m-%d , 而非 %YYYY-%MM-%DD

# 2、datetime.datetime 对象转换成固定时间格式：
# 1）datetime.datetime对象.strftime('%Y-%m-%d')
# 2）datetime.datetime.strftime(datetime.datetime对象,'%Y-%m-%d')

# 3、创建datetime.date类型日期：
# datetime.date(年，月，日)

# 4、datetime.timedelta 时间差对象：
# 1）根据datetime.timedelta()参数指引，可以对date对象，或datetime.datetime对象做时间差的加减运算

# 5、datetime.date对象的replace方法
# 1）可以根据date.replace()方法中的参数指引，替换date对象的年/月/日



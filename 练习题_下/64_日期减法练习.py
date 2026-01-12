# 定义一个函数，接收两个参数：一个'YYYY-MM-DD'格式的日期字符串 pdate，以及一个整数days. 该函数计算从给定日期向前回溯days天后的新日期

import datetime
import time

def find_date(pdate,days):
    int_datetime_struct = datetime.datetime.strptime(pdate,'%Y-%m-%d')
    new_datetime = int_datetime_struct - datetime.timedelta(days=days)
    print(type(new_datetime))
    new_date = new_datetime.strftime('%Y-%m-%d')
    return new_date


pdate = input('请输入日期，格式是 YYYY-MM-DD：')
days = int(input('请输入回溯的天数：'))
print(f'{find_date(pdate,days)}')


# ----- 总结 ---------
# 1、字符串类型转换为datetime类型：
# datetime.datetime.strptime(时间字符串,'前面字符串对应的时间格式')
#
# 2、datetime类型(或date类型)
# 才可以与time.delta类型加减，实现向前或向后追溯
#
# 3、datetime类型时间，转换为时间字符串：
# 1）datetime.datetime.strftime('时间字符串','前面时间字符串对应的时间格式')
# 2）datetime格式时间.strftime('要转换成的时间格式')

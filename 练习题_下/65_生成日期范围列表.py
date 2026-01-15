# 定义一个函数，接收两个"YYYY-MM-DD"格式的日期字符串参数，begin_date 和 end_date，生成一个从开始日期到结束日期(都包含)所有日期的列表，并返回。

import datetime

def time_range(begin_date,end_date):
    begin_date = datetime.datetime.strptime(begin_date,'%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date,'%Y-%m-%d')
    time_list = []
    mid_time = begin_date
    while True:
        if mid_time <= end_date:
            time_list.append(mid_time.strftime('%Y-%m-%d'))
            mid_time += datetime.timedelta(days = 1)
        else:
            break
    return time_list


print(time_range('2026-01-01','2026-01-10'))

# ------ 总结 --------
# 1、字符串转时间格式：
# 1）转换用的方法：datetime.datetime.strptime(时间字符串，'前面时间字符串对应的时间格式')
# 2）时间格式向前向后，用datetime.timedelta(days=n)
# 3）
# 1> 时间格式转字符串：datetime格式时间.strftime('时间格式')
# 2> 另一个方法见前面总结

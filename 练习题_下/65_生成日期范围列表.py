# 定义一个函数，接收两个"YYYY-MM-DD"格式的日期字符串参数，begin_date 和 end_date，生成一个从开始日期到结束日期(都包含)所有日期的列表，并返回。

import datetime

def time_range(begin_date,end_date):
    begin_date = datetime.datetime.strptime(begin_date,'%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date,'%Y-%m-%d')
    time_list = []
    mid_time = begin_date
    while True:
        if mid_time <= end_date:
            time_list.append(mid_time)
            mid_time += datetime.timedelta(days = 1)
        else:
            break
    return time_list


print(time_range('2026-01-01','2026-01-10'))

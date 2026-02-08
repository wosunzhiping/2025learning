# 定义一个函数，用于验证给定的日期字符串是否符合YYYY-MM-DD的格式

import re

date1 = "2026-02-07"
date2 = '202-02-07'
date3 = "2026/02-07"
date4 = "20260207"
date5 = "202a-02-07"


# -------- 我的答案 -------------
# def is_formated(date):
#     try:
#         if 0<int(date[0:4])<9999 and 0<int(date[5:7])<13 and 0<int(date[8:])<32 and date[4]==date[7]=='-':
#             print(f'{date}符合YYYY-MM-DD的格式')
#         else:
#             print(f'{date}不符合YYYY-MM-DD的格式')
#     except Exception as e:
#         print(f'{date}不符合YYYY-MM-DD的格式')
#
#
# is_formated(date1)
# is_formated(date2)
# is_formated(date3)
# is_formated(date4)
# is_formated(date5)


# ------- 参考答案 ------------
def is_right(date):
    return re.match(r'\d{4}-\d{2}-\d{2}',date) is not None


print(date1,is_right(date1))
print(date2,is_right(date2))
print(date3,is_right(date3))
print(date4,is_right(date4))
print(date5,is_right(date5))
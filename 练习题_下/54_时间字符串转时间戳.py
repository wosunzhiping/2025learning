# 给定一个表示时间的字符串，将其转换为以秒为单位的整数时间戳
# a1 = '2025-12-30 22:56:24'
# a2 = '2025/12/30 22:56:24'

import time


a1 = '2025-12-30 22:56:24'
a2 = '2025/12/30 22:56:24'

a1_result = time.mktime(time.strptime(a1,'%Y-%m-%d %H:%M:%S'))
print(time.strptime(a1,'%Y-%m-%d %H:%M:%S'))
print(int(a1_result))

a2_result = time.mktime(time.strptime(a2,'%Y/%m/%d %H:%M:%S'))
print(int(a2_result))

str_now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print(str_now)




# ---------- 总结 ----------
# 1、将某格式的时间字符串转换成时间数组：
#   time.strptime(a1,'%Y-%m-%d %H:%M:%S'))
# 2、将时间数组转换成某格式的时间字符串
#   time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# 3、将时间数组转换为时间戳，是以秒为单位的
#   time.mktime(时间数组)
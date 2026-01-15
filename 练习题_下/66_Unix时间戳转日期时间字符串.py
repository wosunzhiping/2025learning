# 给定一个Unix时间戳，将其转换为对应的日期时间字符串，格式为"YYYY-MM-DD HH:MM:SS"


# ------ 我的答案 ------------------
# import time
#
# unix_time = 1620747224
#
# struc_time = time.gmtime(unix_time)
# print(struc_time,type(struc_time))
#
# f_time = time.strftime('%Y-%m-%d %H:%M:%S',struc_time)
# print(f_time,type(f_time))



# ------ 参考答案 ------------------
import datetime

unix_time = 1620747224

datetime_time = datetime.datetime.fromtimestamp(unix_time)
print(datetime_time,type(datetime_time))

str_time = datetime_time.strftime('%Y-%m-%d %H:%M:%S')
print(str_time,type(str_time))



# --------- 总结-----------
# 1、time模块
# 1）unix时间戳变time.struct_time格式：
# time.gtime(时间戳)

# 2）time.struct_time格式变字符串格式：
# time.strftime('%Y-%m-%d %H:%M:%S',struc_time)
#
# 2、datetime模块
# 1）unix时间戳变datetime.datetime格式：
# datetime.datetime.fromtimestamp(unix_time)
#
# 2）datetime.datetime格式变时间字符串格式：
# datetime_time.strftime('%Y-%m-%d %H:%M:%S')
# 另一个方式见前面总结



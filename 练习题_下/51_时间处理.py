# 编写一个程序，用time模块实现时间处理功能

import time

# 1、当前时间戳，从1970年1.1日0点开始到现在的秒数
print('1、',time.time())



# 3、将时间戳转(默认当前时间戳)换为本地时间的struct_time对象，年 月 日 时 分 秒
# time.struct_time(tm_year=2025, tm_mon=12, tm_mday=24, tm_hour=15, tm_min=53, tm_sec=33, tm_wday=2, tm_yday=358, tm_isdst=0)
print('2、',time.localtime())
print('3、',time.localtime(1766562813.444347))
print(type(time.localtime()))


# 4、将时间戳转换为UTC时间的 struct_time 对象
print('4、',time.gmtime())
print('5、',time.gmtime(1766562813.444347))

# 2、将时间戳转换为本地时间的字符串表示，不传参数默认当前时间  Wed Dec 24 15:50:35 2025
print('6、',time.ctime())
print('7、',time.ctime(1766562813.444347))
print(type(time.ctime()))

# 5、将struct_time对象转换为 星月日时分秒年 格式的字符串表示
print('8、',time.asctime())
print('9、',time.asctime(time.localtime()))
print('10、',time.asctime(time.gmtime()))
print(type(time.asctime()))
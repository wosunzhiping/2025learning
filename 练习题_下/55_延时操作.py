# 程序在暂停1s后获取当前系统时间，并将其打印成'YYYY-MM-DD HH:MM:SS'格式的字符串打印


import time

time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))




# ---------- 总结 -----------
# 1、易错点：时间格式字符串中：
# 1）要有%
# 2）大小写要严格遵守不能错
# 3）字母都是只有一个，不是多个
# 输入一个字符串数据，将其所有小写字母转换为大写，并保存到磁盘文件

import os

input_string = input('请输入一个字符串：')

with open('test.txt','w',encoding='utf-8') as f:
    f.write(input_string.upper())


# ------ 总结 -------
# 1、将字符串中的小写字母转换为大写：
# input_string.upper()

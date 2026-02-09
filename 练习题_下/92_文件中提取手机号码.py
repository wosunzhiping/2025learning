# 从phone.txt 文件中提取并输出所有符合格式的中国手机号码


import re

file_path = '/Users/zhipingsun/Documents/GitHub/2025learning/练习题_下/phone.txt'
pattern = r'1[3-9]\d{9}'
with open(file_path,'r',encoding='utf-8') as f:
    # for line in f.readlines():
    #     res = re.search(pattern,line)
    #     if res is not None:
    #         print(res.group())

    # --- 或者 ：
    res = re.findall(pattern,f.read())
    print(res)



# ----- 总结 ---------
# 1、re.findall(pattern,字符串)：输出的是list
# 2、re.search(pattern,字符串)：能匹配则可使用res.group()得到字符串，不能匹配则输出None
# 3、读取文本文件：
# 1）f.readlines()得到的是list,
# 2）f.read()得到的是所有行组成的一个字符串
# 给定一段包含购物信息的文本，要求提取每样物品的购买数量、物品名、所花费的金额

import re
content = '''
小明上街买菜  
买了1斤黄瓜花了8元；
买了2斤葡萄花了13.5元；
买了3斤白菜花了5.4元；
买了4斤桃花了6.3元
'''

# --------- 我的答案 -------------
# content_list = content.split('\n')
# for line in content_list:
#     count = re.search('\d+斤',line)
#     name = re.search('斤\w+花了',line)
#     price = re.search('\d+(\.\d+)?元',line)
#     if count:
#         print(count.group(),name.group()[1:-2],price.group())


# -------- 参考答案 --------------
pattern = '(\d+)斤(\w+)花了(\d+(\.\d+)?)元'
for line in content.split('\n'):
    res = re.search(pattern,line)
    if res:
        print(res.group())
        print(res.group(0))
        print(res.group(1))
        print(res.group(2))
        print(res.group(3))
        print(res.group(4))

# -------- 总结 --------
# 1、正则表达式模式可以这样写：
# '(\d+)斤(\w+)花了(\d+(\.\d+)?)元'
# 1）把一个字符串中所有要提取的内容用()中写正则表达式的方式替换掉
# 2）用res.group()得到的是整个字符串匹配后的内容
# 3）用res.group(1)得到的是匹配到的第一个()中的内容，以此类推
# 4）如果()中还有()，用res.group(继续后面的编号)可以获得
# 5）用res.groups()得到的是所有()中正则表达式匹配到的字符串组成的list


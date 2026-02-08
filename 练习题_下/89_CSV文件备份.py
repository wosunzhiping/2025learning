# 从人员信息.csv 文件中读取内容，并将其完整复制到另一个csv文件中

import csv

# data = [
#     ["name", "password", "age", "address"],
#     ["张三", "123456", "15", "四川"],
#     ["李四", "111111", "18", "湖南"],
#     ["王五", "888888", "37", "广西"],
#     ["赵六", "666666", "29", "广东"]
# ]
#
# with open('人员信息.csv', 'w', newline='', encoding='utf-8-sig') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)



with open('人员信息.csv','r',encoding='utf-8') as f:
    # print(f.read())
    reader = csv.reader(f)

    # print(reader)

    # for row in reader:
    #     print(row)

    # for line in f.readlines():
    #     print(line)

#     data = [row for row in reader]
#     print(data)
#
# with open('人员信息备份.csv','w',newline='',encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)


# -------- 总结 -------
# 1、处理.csv文件：
# 1）可以用之前处理文本文件一样的f.readlines() 和 f.write()方法，

# 2）可以用csv模块中的方法：
#   1》reader = csv.reader(f)
#      for row in reader:
#          print(row)得到的是每一行的列表，元素是每一格的字符串
#   2》with open('人员信息备份.csv','w',newline='',encoding='utf-8') as f:
#          writer = csv.writer(f)
#          writer.writerows([[第一行单元格组成的列表],[第二行单元格组成的列表],[],[]])
#       其中newline=''表示处理换行符的时候不保留空行


# 2、构造列表：
# data = [row for row in reader]




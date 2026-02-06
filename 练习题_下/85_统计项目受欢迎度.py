# 从student_like.txt 文件中读取学生喜欢的项目列表，统计各项目的受欢迎度

import os

dir = '/Users/zhipingsun/Documents/GitHub/2025learning/练习题_下'
file_path = os.path.join(dir,'student_like.txt')
sport_count = {}

with open(file_path,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.replace('\n','').split()
        # print(line)
        for i in range(1,len(line)):
            if line[i] not in sport_count:
                sport_count[line[i]] = 0
            sport_count[line[i]] += 1
print(sport_count)

sorted_sport = sorted(sport_count.items(),key=lambda x:x[1],reverse=True)
print(sorted_sport)


#-------- 总结 ------------
# 1、拼接文件完整路径：
# file_path = os.path.join(dir,'student_like.txt')

# 2、读取文件内容惯用写法：得到元素是字符串的列表list
# with open(file_path,'r',encoding='utf-8') as f:
#     for line in f.readlines():
#         line = line.replace('\n','').split()  # split括号内无内容，表示按空格或\t分割

# 3、判断键是否在字典中：
# if xxx in dict: 或 if xxx not in dict:

# 4、对字典排序：
# sorted(sport_count.items(),key=lambda x:x[1],reverse=True)
# 1）sport_count.items() 将键值对分解成元组，然后组成类似列表的item对象
# 2）lambda x:x[1] 是获取类列表中的每个元组中的索引为1的内容






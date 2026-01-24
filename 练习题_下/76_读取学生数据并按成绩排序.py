# 从 student_grade_file.txt 文件中读取学生数据(学号、姓名、成绩)，并根据成绩进行排序


# --- 我的答案 起始 -------

# with open('student_grade_file.txt','r',encoding='utf-8') as f:
#         list_init = f.readlines()
#
# list2 = []
# list3 = []
# for i in range(len(list_init)):
#     list2.append(list(list_init[i].replace('\n','').split(',')))
#     list3.append(list2[i][0].split('，'))
# print(list3)
# list4 = sorted(list3,key=lambda x:x[2],reverse=True)
# # print(list4)
#
#
# with open('student_grade_file_sorted.txt','w',encoding='utf-8') as f:
#     for i in list4:
#         f.write('，'.join(i) + '\n')


# --- 我的答案 终止 -------




# --- 参考答案 起始 -------

# 封装三个方法：读取文件、信息排序、写入文件

def read_file():
    # 作用： 读取文件
    # 入参：无需
    # 返参：读取的数据列表
    result = []
    with open('student_grade_file.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            line = line[:-1]
            line = line.split('，')
            result.append(line)
    return result

def sort_info(lst):
    result = sorted(lst,key=lambda x:x[2],reverse=True)
    return result

def write_to_file(lst):
    with open('student_grade_file_sorted.txt','w',encoding='utf-8') as f:
        for line in lst:
            f.write('，'.join(line)+'\n')

# --- 参考答案 终止 -------




# -------- 总结 ---------
# 1、将 字符串 转换成 列表：split('，')：
# 源值：str = '101，小张，88'
# 目标：list = ['105', '小强', '55']
# 操作：str.split('，')

# 2、将 列表 转换成 字符串：
# 源值：list = ['105', '小强', '55']
# 目标：str = '101，小张，88'
# 操作：'，'.join(list)

# 3、排序：针对列表内容
# 方法：sorted(列表,key=lambda x:x[2],reverse=True)
# key=后面的lambda函数是针对列表中每个元素要执行的内容

# 4、f.write写入文件：
# 1）列表不可以用此方法写入文件，只有字符串可以
# 2）写入每一行后，要拼接换行


# 5、f.readlines()
# 得到的是每一行字符串形成的列表list

# 6、字符串替换：
# s.replace('\n','')


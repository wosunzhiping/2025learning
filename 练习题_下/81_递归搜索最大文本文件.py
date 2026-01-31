# 搜索指定目录(含其子目录)内的所有.txt文件，并找出其中最大的文件及其大小

import os


# ------- 我的答案 ----------------
max_file_size = 0
max_file_path = ''
dir = '/Users/zhipingsun/Documents/GitHub/2025learning'  # 或者写成这样的形式 dir = r'D:\Python'  r用于取消转译
for root,dirs,files in os.walk(dir):
    for file in files:
        full_file_name = os.path.join(root,file)  # 构造完整路径，可以用 full_file_name = f'{root}/{file}'
        extend_name = os.path.splitext(file)[1][1:]   # 判断是否以.txt结尾，可以用 file.endswith(".txt")
        if os.path.isfile(full_file_name) and extend_name == 'txt':
            current_file_size =  os.path.getsize(full_file_name)
            if  current_file_size > max_file_size:
                max_file_size = current_file_size
                max_file_path = full_file_name

print(f'最大的文件是：{max_file_path},大小为{max_file_size/1024:.2f}')  # 还可以将文件路径及大小作为元组append到列表，然后用sorted方法排序


# --------------- 参考答案 --------------------
# dir2 = '/Users/zhipingsun/Documents/GitHub/2025learning'
# file_size_list = []
# for root,dirs,files in os.walk(dir2):
#     for file in files:
#         if file.endswith('.txt'):
#             full_file_name_new = f'{root}/{file}'
#             file_size = os.path.getsize(full_file_name_new)/1024   # 这里不能用:.2f，只有在f''的输出方式时才可以使用
#             # print(full_file_name_new)
#             file_size_list.append((full_file_name_new,file_size))
# sorted_list = sorted(file_size_list,key=lambda x:x[1],reverse=True)
# # print(sorted_list)
#
# print(f'最大的文件是：{sorted_list[0][0]},大小为{sorted_list[0][1]:.2f}')





# --------- 总结 -------------
# 1、目录字符串可以写成：
# dir = r'D:\Python'
# r用于取消转译


# 1、递归遍历目录下所有文件：
# for root,dirs,files in os.walk(文件目录)
# 1) root 当前遍历的目录路径
# 2）dirs 当前目录下的所有子文件夹名称组成的列表
# 3）files 当前目录下的所有文件名构成的列表
# 4）这个方法会让root递归搜索完所有文件夹，所以在这个for循环中只需要使用files，就是拿到了目录下包括所有子文件夹中的文件。

# 2、构造文件的完整路径：
# 1）full_file_name = os.path.join(root,file)
# 2) full_file_name = f'{root}/{file}'

# 3、判断文件的扩展名：
# 1）extend_name = os.path.splitext(file)[1][1:]
# 2）file.endswith(".txt")

# 4、获取文件大小：单位是B，变成KB的话需要除以1024
# os.path.getsize(文件完整路径)

# 5、注意保留两位小数输出 :.2f 的使用：
# 1）只有在f'' 字符串输出的格式中使用，
# 2）file_size = os.path.getsize(full_file_name_new)/1024  这里只是计算数值，并未输出字符串，不能用:.2f

# 6、涉及到排序 --> 考虑构建元素为元组或列表的列表，然后用sorted方法实现(含lambd函数)

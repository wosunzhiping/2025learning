# 将指定目录下所有.txt文件内容合并到一个新的文件中，每个文件的内容之间用换行符分割

import os



#   ----------- 我的答案 ------------

# def merge_files(file_list,out_file):
#     for file_t in file_list:
#         with open(file_t,'r',encoding='utf-8') as fr:
#             for line in fr.readlines():
#                 # print(line)
#                 with open(out_file, 'a', encoding='utf-8') as f:
#                     f.write(line)
#         with open(out_file, 'a', encoding='utf-8') as f:
#             f.write('\n')
#
# dir = '/Users/zhipingsun/Documents/GitHub/2025learning/练习题_下'
#
# init_files = []
# files = os.listdir(dir)
# for file in files:
#     if file.endswith('.txt'):
#         # print(file)
#         full_file = os.path.join(dir,file)
#         init_files.append(full_file)
#
# out_file = os.path.join(dir,'out.txt')
#
# merge_files(init_files,out_file)




# --------- 参考答案 -------

dir = '/Users/zhipingsun/Documents/GitHub/2025learning/练习题_下'
context = []

for file in os.listdir(dir):
    full_path = f'{dir}/{file}'
    if os.path.isfile(full_path) and file.endswith('.txt'):
        with open(full_path, 'r', encoding='utf-8') as f:
            context.append(f.read())

out_file = os.path.join(dir,'out2.txt')

with open(out_file,'w',encoding='utf-8') as f:
    for cont in context:
        f.write(cont + 2*'\n')


# ----------- 总结 -------------
# 1、遍历文件夹下所有文件夹及文件：
# os.listdir(目录)
#
# 2、判断是否是文件：
# os.path.isfile(文件)
# 其中文件是绝对路径
#
# 3、判断文件是txt文件：
# file.endswith('.txt'):
#
# 4、多个文件的内容用f.read()读取，添加到列表，再从列表读取写到文件
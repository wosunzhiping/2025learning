# 编写一个程序，计算当前目录下所有文件的大小总和，并将结果以千字节(KB)为单位打印


# ------ 我的答案 --------
# from pathlib import Path
#
# def get_file_size(directory):
#     file_size = {}
#     for file in Path(directory).rglob('*'):
#         if file.is_file():
#             file_size[file.name] = file.stat().st_size
#
#     return file_size
# result_dict = get_file_size('/Users/zhipingsun/Documents/GitHub/2025learning')
#
# print(sum(result_dict.values()))



# ------- 参考答案 ----------
import os

sum = 0
for file in os.listdir():
    if os.path.isfile(file):
        sum += os.path.getsize(file)
print(f'{sum/1024/1024:.2f}MB')

# os.path.getsize()



# ------ 总结 --------
# 1、判断路径是否存在，且为文件：
# os.path.isfile(文件名)

# 2、获取目录下所有的文件及文件夹：
# os.listdir()
# 1）括号中不填，默认查找当前目录
# 2）输出为list，元素是文件及文件夹的名称字符串

# 3、获取文件的大小：
# os.path.getsize(文件名)
# 1）得到的结果单位是字节
# 2）需要除以1024得到KB
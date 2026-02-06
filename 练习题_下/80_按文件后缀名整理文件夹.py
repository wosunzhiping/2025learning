# 遍历指定目录下的所有文件，并根据每个文件的后缀名进行分类

import os
import shutil  # 用于文件的移动

dir = '/Users/zhipingsun/Documents/GitHub/2025learning/dirTest'
dir2 = '/Users/zhipingsun/Documents/GitHub/2025learning/练习题_下'


for file in os.listdir(dir):
    full_file_name = os.path.join(dir, file)
    if os.path.isfile(full_file_name):
        extend_name = os.path.splitext(file)[1][1:]
        if extend_name:
            dir_name = os.path.join(dir,extend_name)  # 或者直接用字符串拼接,拼接中用斜杠 f'{dir}/{file}'
            if not os.path.exists(dir_name):
                os.mkdir(dir_name, mode=0o777)
            shutil.move(full_file_name,dir_name)


        # print(os.path.splitext(file)[1])

# shutil.move('chatlog.txt','/Users/zhipingsun/Documents/GitHub/2025learning1/')


# --------- 总结 -----------
# 1、获取指定目录下的所有文件和文件夹：
# os.listdir('路径')

# 2、判断是否是文件(而非文件夹)：
# os.path.isfile(full_file_name)
# 1）参数要用完整文件名
# 2）完整文件名拼接方法：os.path.join(目录，文件名)

# 2、获取文件后缀名：
# os.path.splitext(file)[1][1:]
# 1）这里的file不用使用完整目录
# 2）os.path.splitext(file)得到的是一个个元组
# 3）[1:] 字符串切片，获取没有.的后缀名

# 3、判断文件夹是否存在：
# os.path.exists(full_dir_name)
# 1）参数要使用完整路径+文件夹名称

# 4、完整路径拼接方法：
# 1）完整文件夹名称拼接方法：
#   os.path.join(目录，文件夹名)
# 2）完整文件名拼接方法：
#   os.path.join(目录，文件名)
# 3）注意：
# 目录名字符串，最后没有\，使用上述方法拼接的时候，会自动加\


# 5、移动文件到文件夹：
# shutil.move(full_file_name,dir_name)
# 1）文件名要使用完整文件名，否则会在当前目录下找文件名
# 2）该操作是移动文件，不是复制文件

# 6、创建文件夹：
# os.mkdir(dir_name,mode=0o777)
# 1）文件夹名称需是完整文件夹路径，否则会在当前目录下创建文件夹
# 2）mode=0o777

# 7、连贯写法：
# for file in os.listdir(dir):
#     full_file_name = os.path.join(dir, file)




# 不断提示用户输入数据，直到输入结束符"#"，在输入过程中，将用户每次输入的数据逐行保存到文件中
import os

def write_to_file(file_name,content):
    dir = '/Users/zhipingsun/Documents/GitHub/2025learning/练习题_下'
    full_name = os.path.join(dir,file_name)
    with open(full_name,'a',encoding='utf-8') as f:
        f.write(content)

while True:
    cont = input('请输入数据：')
    if cont != '#':
        write_to_file('user_input.txt',cont+'\n')
    else:
        break


# --------- 总结 --------
# 1、用追加的方式写入文件：用'a'
# with open(full_name,'a',encoding='utf-8') as f:

# 2、循环次数不知道，结束的条件知道，用
# while True:

# 3、追加写入文件，注意每一行后面要加'\n'
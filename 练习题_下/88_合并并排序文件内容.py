# text1.txt 和 text2.txt 两个文件中各存着一行字母。将这两行字母合并，并按字母顺序排序，将排序后的结果写入test3.txt中
import os

dir = '/Users/zhipingsun/Documents/GitHub/2025learning/练习题_下'
# full_path_1 = os.path.join(dir,'test1.txt')
# full_path_2 = dir + '/test2.txt'

test1 = []
test2 = []
# ----------------- 我的答案 -------------------------
# with open('test1.txt','r',encoding='utf-8') as f:
#     for i in f.readline():
#         test1.append(i)
# with open('test2.txt','r',encoding='utf-8') as f:
#     for j in f.readline():
#         test2.append(j)
#
# test3 = test1 + test2
# print(test3)
#
# sorted_test = sorted(test3,key=lambda x:x,reverse=True)
# print(sorted_test)
#
# with open('test3.txt','a',encoding='utf-8') as f:
#     for i in sorted_test:
#         f.write(i)


# ------------- 参考答案:差异化部分 -----------------
def read_file(path):
    with open(path,'r',encoding='utf-8') as f:
        return f.read()

test1 = read_file('test1.txt')
test2 = read_file('test2.txt')
combine_text = test1 + test2
print(combine_text)
sorted_text = sorted(combine_text)
print(sorted_text)
sorted_result = ''.join(sorted_text)
print(sorted_result)



# ------- 总结 -------
# 1、读出文件全部内容：
# f.read()

# 2、排序字符串：可以直接用sorted()方法
# 1）sorted(combine_text)
# 2）字符串的排序结果是每个字母作为字符串元素的列表list
# 3）将列表拼接成字符串，中间没有任何字符：''.join(sorted_text)

# 3、字符串拼接，是可以直接用+的：
# combine_text = test1 + test2

# 统计文件中各个单词出现的次数，并将出现次数最多的前十个单词及其对应的次数输出
import re

def read_file():
    word_dic = {}
    with open('english.txt','r',encoding='utf-8') as f:
        page = f.read()
        res = re.split('\s+',page)  # 不是\n。缺点是，注意\s+表示切割时去掉一个或多个空格
        print(res)
        for word in res:
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1
    sorted_items = sorted(word_dic.items(),key= lambda x:x[1],reverse=True)
    sorted_dic = {k:v for k,v in sorted_items}
    # print(sorted_dic)

    for k,v in list(sorted_dic.items())[:10]:
        print(f'{k}:{v}')
read_file()



# ------ 参考答案 ---------
word_dic = {}
with open('english.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line[:-1]    #当最后一行没有换行符的时候，这样处理会丢失最后一行的最后一个字符
        line = line.split()
        for word in line:
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1
# print(word_dic.items())
word_sorted = sorted(word_dic.items(),key=lambda x:x[1],reverse=True)[:10] # word_dic.items(), 是dict_items类型的一个list，
print(word_sorted)


# ------ 总结 --------
# 1、字符串切片：
# line = line[:-1] 字符串line的开始到倒数第一位截止(不含)

# 2、按空格或换行符分割字符串，形成列表：
# line = line.split()
# 1）split()中什么都不写，表示空格和换行符；
# 2）不能用split('\s')，\s这个只有在re正则表达式库中才表示空格；
# 3）效果跟re.split('\s+')一样(不过这个不含对\t的分割效果)
# 4）re.split('\s+') 得到的也是一个list，元素是被分割出来的一个个字符串

# 3、re.split()

# 3、sorted()可以对字典排序：
# word_sorted = sorted(word_dic.items(),key=lambda x:x[1],reverse=True)[:10]
# 1）word_dic.items() ：将字典中的键值对转换成类似列表中的元组。
# 2）key=lambda x:x[1] 因为word_dic.items()中每一个元素是元组，可以通过x[1]这样的索引来访问
# 3）[:10]类似切片，是对已排序的列表选取第0到第9项

# 4、判断某个键是否存在于字典中，用in：
# if word in word_dic:
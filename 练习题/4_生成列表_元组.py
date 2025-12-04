# 举例：控制台输入：34岁，67年，99人，25个，11月，则输出列表和元组：['36','67','99','25','11']('36','67','99','25','11')
import re

def to_numlist(ini_list):
    num_list = []
    for i in ini_list:
        num_list.append((re.match('\d*',i)).group())
    return num_list


if __name__ == '__main__':
    print('请输入含数字序列的信息：')
    str = input()


    #--------我的答案---------
    ini_list = str.split('，')
    to_numlist(ini_list)
    print(to_numlist(ini_list))
    print(tuple(to_numlist(ini_list)))

    #--------参考答案---------
    # l = re.findall('\d+',str)   这样写也可以
    l = re.findall(r'[0-9]+',str)
    print(l)
    print(tuple(l))


#----------总结------------
# 1、tuple 元组没有append()方法
# 2、列表转元组直接用tuple(列表)
# 3、循环中将元素追加到列表中，不用num_list = num_list.append() 这种错误写法，直接是 num_list.append()
# 4、for i in list 循环中，i本身就是list中的元素了，不要把i作为list的索引
# 5、(re.match('\d*',i)).group()
# 6、re.findall('正则表达式','目标字符串')，将满足条件的字符串以列表的形式输出
# 7、正则表达式，re.findall('\d+',str)    跟 re.findall(r'[0-9]+',str)  等效
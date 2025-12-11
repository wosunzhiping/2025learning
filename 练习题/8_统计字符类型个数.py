# 输入一行字符，统计其中字母、空格、数字和其他字符的个数。
import re

if __name__ == '__main__':

# ------ 我的答案 ------
#     print('请输入一行字符：')
#     l = input()
#     en_list = re.findall('[a-z]|[A-Z]',l)
#     s_list = re.findall('\s',l)
#     d_list = re.findall('\d',l)
#
#     print(f'英文字母的个数是{len(en_list)}')
#     print(f'空格的个数是{len(s_list)}')
#     print(f'数字的个数是{len(d_list)}')


# ----- 参考答案 -------
    s = input('请输入一行字符：')
    num_alpha = 0
    num_digit = 0
    num_space = 0
    num_other = 0
    for c in s:
        if c.isalpha():
            print('这是字母类型：',c)
            num_alpha += 1
        elif c.isdigit():
            print('这是数字：',c)
            num_digit += 1
        elif c.isspace():
            print('这是空格：',c)
            num_space += 1
        else:
            print('这是其他字符：',c)
            num_other += 1
    print(f'英文字母有{num_alpha}个，数字有{num_digit}个，空格有{num_space}个，其他字符有{num_other}个')


# --- 总结 --------
# 1、内置函数：
# isalpha() 字符串中是否仅包含英文(汉字也视为字母字符);
# isdigit() 字符串中是否仅包含数字；
# isspace() 字符串中是否仅包含空格；
# isupper() 字符串中是否全为大写，或者至少有一个大写字母，且没有小写字母、没有非字母字符；
# islower() 字符串中是否全为小写，或者至少有一个小写字母，且没有大写字母、没有非字母字符；
# istitle() 字符串是否以大写字母开头
# 2、for c in s : 是遍历字符串中的每一个字符
# 3、re.findall('正则表达式','目标字符串')  输出的是满足条件的列表list，注意正则表达式中不要放()

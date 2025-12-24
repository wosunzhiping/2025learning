# 从用户指定的数字范围内随机选择3个不重复的数字
import random

def no_repeat_num(lst):
    result = ''
    for i in range(3):
        s = random.choice(lst)
        if s in result:
            continue
        result += s
    return result

list = ['1','2','3','4','5','6']

print(no_repeat_num(list))
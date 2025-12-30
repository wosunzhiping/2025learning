# 从用户指定的数字范围内随机选择3个不重复的数字
import random


# --------- 我的答案 -----------------
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


# --------- 参考答案 -------------
start = int(input('请输入数字范围的起始值：'))
end = int(input('请输入数字范围的结束值：'))
# result = random.sample([i for i in range(start,end+1)],3)
result = random.sample(range(start,end+1),3)
print(result)

# -------- 总结 -------
# 1、range(a,b) 内置序列类型，是一个不可变的序列，
# 1）表示从a到b-1之间的整数序列，但不是列表，它是一个特殊的序列类型
# 2）支持索引、切片、长度计算，
# 3）不支持序列的+和*操作，因为它的元素不可变
#
# 2、random.sample(序列，n)：
# 1）作用：从指定的序列中不重复的选择n个元素
# 2）返回的是一个列表3
#
# 、列表推导式：[i for i in range(start,end+1)]

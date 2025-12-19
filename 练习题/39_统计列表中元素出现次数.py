# 定义一个函数，用于统计指定元素在指定列表中出现的次数

def count_of_num(lst,n):
    if len(lst) == 0:
        print('指定列表为空')
        return lst

    count = 0
    for i in range(0,len(lst)):
        if lst[i] == n:
            count += 1
    return count

l1 = [1,2,3,4,3,4,3,4]
n = 4

print(f'指定列表{l1}中指定元素{n}的个数是：{count_of_num(l1,n)}')

print(f'指定列表{l1}中指定元素{n}的个数是：{l1.count(n)}')


# ------- 总结 --------
# 1、注意：
#   返回count的位置，是在循环结束后，所以缩进应该跟if对齐
# 2、列表的内置函数：
#   list.count(n)
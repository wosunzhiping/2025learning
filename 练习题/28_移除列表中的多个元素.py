# 定义一个函数，用于从第一个列表list1中移除第二个列表list2中存在的所有元素

# 入参：list1,list2
# 返参：剩余的list

# ------- 方法一：嵌套循环 ----------
# def del_result(list1,list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 list1.remove(i)
#     return list1


# ------- 方法二：使用列表推导式----------
def del_result_1(list1,list2):
    return [i for i in list1  if i  not in list2]

list1 = [3,7,7,9,11,13]
list2 = [7,11]
print(del_result_1(list1,list2))


#-------总结——---------
# 1、列表推导式：[表达式 for 变量 in 可迭代对象 if 条件]
#   return [i for i in list1 if i not in list2]
#   i 不在列表中，用 i not in list2，不是i is not in list2

# 2、删除列表中元素：
#   list.remove(i)  i是列表中的元素，不是索引
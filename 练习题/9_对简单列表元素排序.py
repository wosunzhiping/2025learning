# 给定一个简单列表(元素不是复合类型，如列表/元组/字典)，对其元素进行排序
# 示例：
# 形式1：[20,50,10,40,30]
# 形式2：['bb','ee','aa','dd','cc']

if __name__ == '__main__':

# ---- 我的答案------
#     list = ['bb','ee','aa','dd','cc']
#     for i in range(0,len(list)):
#         for j in range(i+1,len(list)):
#             if list[i] < list[j] or list[i] == list[j]:
#                 continue
#             else:
#                 a = list[i]
#                 list[i] = list[j]
#                 list[j] = a
#     print(list)


# ---- 参考答案 ------
    list = [-20,50,10,40,30]
    list.sort()
    print(list)  # 这里不是 print(list.sort())
    list.sort(key=abs)
    print(list)
    list.sort(reverse=True)
    print(list)

    list1 = sorted(list,key=abs,reverse=True)
    print(list1)



# ----总结----
# 1、sort()：对原列表排序，不返回新列表，直接改变原有列表
# 注意：
# 1）list.sort()值为none, 排序后的列表仍是list。list.sort()是完成了list的重新排序；
# 2）sort(key=None,reverse=False)可以有两个参数，其中
#       key:接收一个函数作为参数，该函数会在每一个元素上调用，结果作为排序的依据；举例见代码
#       reverse 如果为True，则按降序排列，为False，则升序排列；举例见代码
#
#
# 2、sorted()：不改变原列表顺序，排序后生成新列表
# 注意：
# 1）sorted(iterable,key,reverse),有三个参数，第一个为要被排序的原列表，key、reverse跟sort()方法中的定义一样。
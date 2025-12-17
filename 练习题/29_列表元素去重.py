# 定义一个函数，用于对列表元素进行去重处理




# --------- 我的答案 ------------------
def no_mult_list(list):
    list_back = []
    for i in range(0,len(list)):
        for j in range(min((i+1),len(list)),len(list)):
            if list[i]  == list[j]:
                break
        else:
            list_back.append(list[i])
    return list_back


list1=[10,20,30,10,20]
print(no_mult_list(list1))


# --------- 参考答案（一） ------------------
def remove_duplicate(list_init):
    result = []
    for i in list1:
        if i not in result:
            result.append(i)
    return result

list2=[10,20,30,10,20]
print(remove_duplicate(list2))


# --------- 参考答案（二） ------------------
def remove_duplicate_set(list_init):
    return list(set(list_init))

list3=[10,20,30,10,20]
print(remove_duplicate_set(list3))

# --------总结 -----------
# 1、去重的思路：
#   1）对比原有列表中的元素，将不重复的逐项添加到新列表；
#   2）定义新列表，逐项添加原列表的元素，添加的时候对比是否跟本新列表元素重复
# 2、if i not in list:
#   元素不在列表中的写法
# 3、for循环中的else语句：
# 1）如果循环正常结束（没有通过break跳出），则执行else部分；如果通过break跳出循环，则else中的部分也不执行了
# 2）else跟if对齐
# 3）注意：如果要实现for循环完成后所有元素都没有满足if条件，此时要做某个操作，一定要对齐来写else:，不要漏掉 else：

# 3、去重----》 set 集合 支持自动去重
#   将列表转换为set，再转换回列表
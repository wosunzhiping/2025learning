# 给定一个已经排序好的整数列表，输入一个数，根据列表原有的排序规则将其插入正确的位置


if __name__ == '__main__':

# --- 我的答案(考虑到排序可能是从高到低)---------
#     list = [21,33,57,88,95]
#     list1 = sorted(list,reverse=True)
#     list2 = sorted(list,reverse=False)
#     num = int(input('请输入一个整数：'))
#     list.append(num)
#
#
#     if list1 == list:
#         list4 = sorted(list,reverse=True)
#         print(list4)
#     else:
#         list4 = sorted(list,reverse=False)
#         print(list4)



# ------ 参考答案(默认题目序列从小到大)---------
    list = [21, 33, 57, 88, 95]
    num = int(input('请输入一个整数：'))
    for i in range(0,len(list)):
        if list[i] > num:
            list.insert(i,num)
            break
    else:
        list.append(num)
    print(list)


# -----总结-----
# 1、常错点：
#   在list列表中追加元素，不要用 list_new = list.append(num) ,错误的认为 list_new是追加后的列表。实际上它是none。
#
# 2、两个列表是否相等的判断：
#   也可以用这种方式 list1 == list
#
# 3、循环中的else语句：
# 1）如果循环正常结束（没有通过break跳出），则执行else部分；
# 2）else跟if对齐
#
# 4、用索引循环取数：
# for i in range(0,len(list))
#
# 5、列表中插入元素：
# list.insert(i,num)

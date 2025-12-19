# 定义一个函数，用于将指定列表中的指定两个索引位置的元素对调

def change_two_num(list1,m,n):
    if len(list1) <= 1:
        print(f'{list1}不存在两个可以互换的元素')
        return
    if m not in range(0,len(list1)):
        print(f'{m}超出有效索引范围')
        return
    if n not in range(0,len(list1)):
        print(f'{n}超出有效索引范围')
        return

    list1[m],list1[n] = list1[n],list1[m]
    return list1


l1 = [1,2,3,4,5,6,7]
print(change_two_num(l1,3,6))


# --------- 总结 ---------
# 1、元组解包特性，将两个元素互换：
#   list1[m],list1[n] = list1[n],list1[m]
# 2、不在某个范围内：not in range()
#   if m not in range(0,len(list1)):
#   if not 0<= m < len(list1)
# 3、自定义的函数：
# 1）先判断异常场景，直接return，就不会执行其后面的代码；
# 2）后面正常场景的代码，前面就无需用else了
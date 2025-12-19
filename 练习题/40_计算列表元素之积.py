# 定义一个函数，接收一个整数列表，并返回该列表所有元素之积

def product_of_list(lst):
    if len(lst) == 0:
        print('列表为空')
        return


    for i in lst:
        if type(i) != type(1):
            print('列表元素并非全部为整数，请重新输入')
            return
    result = 1
    for i in lst:
        result *= i
    return result


list1 = [1,2,3,4,5]
print(f'列表{list1}的所有元素之积是：{product_of_list(list1)}')


# ----总结 ----
# 1、计算乘积，初始化的值不是0，而是1
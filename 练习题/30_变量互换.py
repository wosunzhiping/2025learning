# 定义一个函数，用于实现两个变量值的互换


# ------ 我的答案 ------------
# def change(x,y):
#     x,y = y,x
#     print(x,y)
#
# x=3
# y=5
# change(x,y)
# print(f'x和y互换后的值分别为：{x}和{y}')  ----- 这样打印的值不是互换的值


# --------- 参考答案 ---------
def swap_values(var1,var2):
    return var2,var1

name1 = 'bbb'
name2 = 'ccc'
name1,name2 = swap_values(name1,name2)

print(swap_values(name1,name2))
print(name1,name2)



# ------- 总结 -------
# 1、返回多个值：是以元组的方式返回
#    return var2,var1
#    打印这个返回值值是 ('bbb', 'ccc')

# 2、接收多个值：元组的解包 直接用给多个变量赋值的方式接收：
#    name1,name2 = ('bbb', 'ccc')

# 3、两个变量互换：
#    可以直接写成 x,y = y,x

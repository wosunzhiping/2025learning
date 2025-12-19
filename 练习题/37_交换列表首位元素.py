# 定义一个函数，接收一个列表元素，交换该列表的第一个元素和最后一个元素，然后返回交换后的列表

def charge_num(list_init):
    if len(list_init) in [0,1]:
        return '该列表无需交换'
    list_init[0],list_init[-1] = list_init[-1],list_init[0]
    return list_init

list=[1,2,3,4,5]
print(charge_num(list))



# ------ 总结 -------
# 1、元组解包特性：
#   在不设置中间变量的情况下，实现多个变量的赋值：list_init[0],list_init[-1] = list_init[-1],list_init[0]
# 2、边界值的处理：考虑函数入参的异常值处理；
#   异常值处理完直接return，可以不用执行其下的其他内容
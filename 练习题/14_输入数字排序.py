# 接收用户输入的三个数字，并按从小到大的顺序输出

if __name__ == '__main__':

# ------我的答案--------
#     str = input('请输入三个数字：')
#     list = str.split(',')
#     list.sort()
#     print('数字从小到大排序是：',','.join(list))


#------参考答案（一）---------
    # num1 = float(input('请输入第一个数字：'))
    # num2 = float(input('请输入第二个数字：'))
    # num3 = float(input('请输入第三个数字：'))
    #
    # if num1 > num2:
    #     num1,num2 = num2,num1
    #
    # if num1 > num3:
    #     num1,num3 = num3,num1
    #
    # if num2 > num3:
    #     num2,num3 = num3,num2
    #
    # print('从小到大排序是：',num1,num2,num3)


#------参考答案（二）---------
    num1 = float(input('请输入第一个数字：'))
    num2 = float(input('请输入第二个数字：'))
    num3 = float(input('请输入第三个数字：'))

    print('从小到大排序是：',sorted([num1,num2,num3]))


# ------ 总结--------
# 1、交换两个数字，可以直接用：num1,num2 = num2,num1
# 2、内置函数，sort() 和 sorted()
# 定义一个函数，用于打印指定范围内的所有素数



# --- 我的答案 ------
# def su(x,y):
#     list = []
#     for i in range(x,y+1):
#         count = 0
#         for j in range(2,i):
#             if  i % j == 0:
#                 count += 1
#                 break
#             else:
#                 continue
#         if count == 0:
#             list.append(i)
#
#     return list
#
#
# if __name__ == '__main__':
#     x = int(input('请输入范围的起始值：'))
#     y = int(input('请输入范围的结束值：'))
#     print(f'范围{x}-{y}内的所有素数是：{su(x,y)}')


# -------------------- 参考答案 --------------------


def is_su(num):
    if num <= 1:
        return False
    # if num == 2:
    #     return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True



def print_su(x,y):
    list = []
    for i in range(x,y+1):
        if is_su(i):
            list.append(i)
    print(f'范围内的素数是：{list}')

for i in range(2,2):
    print('1')



# ------------ 总结 ------------
# 1、编写函数的思考顺序：
#   函数的目的、函数的入参、函数的返参
# is_su(num)
# 函数目的：判断一个数是否是素数
# 函数入参：num
# 函数返参：True 或 False
# print_su(x,y)
# 函数目的：打印一个范围内所有的素数
# 函数入参：范围
# 函数返参：无，直接打印即可

# 2、函数中return的性质，可以被利用：
#   直接返回，后面的内容不再继续，感觉相当于循环中的break，所以当需要满足某条件下就返回的情况，可以考虑定义函数，并用return结束；
#   如果是for循环嵌套if判断，满足条件跳出循环，在方法里就可以直接用return就满足了这个要求，相当于用了break

# 3、for i in range(2,2)
#   这个语句i不会拿到任何值，不会进入循环

# 4、for 循环中嵌套if：
#   如果for循环不是因为if中的break跳出循环，那么它就会持续循环直到for循环结束，然后执行跟for缩紧一致的后续代码块
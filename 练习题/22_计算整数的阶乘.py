# 定义一个函数，用于返回给定整数的阶乘


# ---- 我的答案 --------
# def fac(n):
#     if n == 0:
#         return 1
#     if n<0:
#         return '负数没有阶乘，请重新输入'
#     return n*fac(n-1)
#
# if __name__ == '__main__':
#     num = int(input('请输入一个整数：'))
#     print(f'{num}的阶乘为：{fac(num)}')



# ------参考答案-------
def fac1(n):
    result = 1
    if n<0:
        return '负数没有阶乘'
    else:
        for i in range(1,n+1):
            result *= i
            return result


if __name__ == '__main__':
    n = int(input('请输入一个整数：'))
    print(fac1(n))




# ---- 总结 ----
# 1、递归、循环 两种方式计算

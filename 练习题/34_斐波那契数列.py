# 定义一个函数，用于计算斐波那契数列中的第n项
# 斐波那契数列：前两项都为1，之后的每一项都是前两项之和

def n_of_fbnq(n):
    if n<=0:
        print('n必须为正整数')
        return
    if n in [1,2] :
        return 1
    else:
        return n_of_fbnq(n-1) + n_of_fbnq(n-2)


print(n_of_fbnq(0))



# ------ 总结 --------

# 2、如果输入不正确，
#   print错误信息后，
#   要return None，或者仅return ，默认返回None。这样程序到此退出，不会执行之后的判断
#
# 3、递归：
#    函数的作用是返回第n项的值，那么在函数中使用到返回第n-1项的值的时候，就是调用函数自身，入参为n-1的时候。
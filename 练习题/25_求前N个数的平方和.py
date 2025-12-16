# 定义一个函数，用于计算从1的平方到n的平方的所有整数的平方和


def n_sum(n):
    result = 0
    for i in range(1,n+1):
        result += i**2
    return result


if __name__ == '__main__':
    n = int(input('请输入一个整数：'))
    print(f'从1到{n}所有整数的平方和为：{n_sum(n)}')


# ---- 总结 ---
# 1、平方：i ** 2
# 2、求和：循环前先定义 result = 0
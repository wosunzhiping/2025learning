# 定义一个函数，用于返回给定整数n的倒数序列和。如n为偶数，则返回1/2+1/4+1/6+...+1/n；若n为奇数，则返回1/1+1/3+1/5+1/7+。。。+1/n

def sum_of_reverse(n):
    if n <= 0:
        print('n必须为正整数')
        return None

    sum = 0
    if n % 2 == 0:
        for i in range(2,n+1,2):
            # print(f'1/{i}')
            sum += 1/i
    elif n % 2 == 1:
        for i in range(1,n+1,2):
            # print(f'1/{i}')
            sum += 1/i
    return sum




if __name__ == '__main__':
    n = int(input('请输入一个正整数：'))
    print(f'{n}的倒数序列和为：{sum_of_reverse(n)}')

# --------- 总结 ----------
# 1、自定义的函数中有print命令：
#   1）单独调用函数，会打印；
#   2）在print()中调用，也会正常打印
# 比较两个整型变量，打印比较结果

if __name__ == '__main__':
    print('请输入第一个整数：')
    x = int(input())
    print('请输入第二个整数：')
    y = int(input())
    if x > y:
        print(f'比较结果为：{x} > {y}')
    elif x < y:
        print(f'比较结果为：{x}  < {y}')
    else:
        print(f'比较结果为：{x}  = {y}')

# -----总结------
# 1、我使用了三个if，参考答案使用的是if -- elif --else
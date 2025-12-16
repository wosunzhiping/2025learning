# 用户输入一个数字，实现将十进制转换为二进制、八进制、十六进制，并打印输出

if __name__ == '__main__':
    num = int(input('请输入一个数字：'))
    print(f'二进制转换结果：{bin(num)}')
    print(f'八进制转换结果：{oct(num)}')
    print(f'十六进制转换结果：{hex(num)}')


#-------总结------
# 1、进制转换的内置函数，bin()  oct()  hex()
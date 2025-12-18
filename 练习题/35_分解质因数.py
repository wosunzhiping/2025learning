# 定义一个函数，其接收一个正整数n，将其分解为质因数，并打印输出；
# 例如 传入90，打印 90 = 2*3*3*5



# ----- 我的答案 ----------
# def zhi_num(n):
#     list = []
#     for i in range(2,n):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             list.append(i)
#     return list
#
# def spare_num(n):
#     list = zhi_num(n)
#     result = []
#     mid = n
#     i = 0
#     while i< len(list):
#         if mid % list[i] == 0:
#             mid //= list[i]
#             result.append(list[i])
#         else:
#             i += 1
#     return result
#
#
#
# if __name__ == '__main__':
#     num = int(input('请输入一个正整数：'))
#     print(f'质数有：{zhi_num(num)}')
#     print(f'{num} =  {spare_num(num)}')


# ----- 参考答案 ----------

def num_of_zhi(n):
    i = 2
    while i ** 2 < n:
        if n % i == 0:
            n //= i
            print(i, end='*')
        else:
            i += 1
    if n>1:
        print(n)

if __name__ == '__main__':
    num = int(input('请输入一个正整数：'))
    print(f'{num}=',num_of_zhi(num))

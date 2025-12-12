# 如果用户输入3，程序应输出  最小的由n个9组成的、能被3整除的数，并输出 9/3=3.0
# 如果用户输入11，程序应输出  最小的由n个9组成的、能被11整除的数，并输出 99/11=9.0


if __name__ == '__main__':
    num = int(input('请输入一个奇数：'))


# ---- 我的答案 --------
#     for i in range(9,(num+1)*9,9):
#         if i%num == 0:
#             print(f'最小的由{i/9}个9组成的数能被{num}整除，{i}/{num}={i/num}')
#             break



# ---- 参考答案 --------
    n = 1
    while True:
        n_num = int(n * '9')
        if n_num % num == 0:
            print(f'最小的由{n}个9组成的数能被{num}整除，{n_num}/{num}={n_num/num}')
            break
        else:
            n += 1


# -------总结-------
# 1、while True的使用：循环次数未知，但结束条件已知
# 2、连续字符串：(n * '9')
# 3、while True循环中if条件满足后break，跳出循环；如果不是通过break退出，则循环永远进行，所以if条件不满足则执行else，else跟if对齐来写
# 与for循环中不同：for循环中if条件满足后break，则跳出循环；但存在for循环循环完了，if条件都不满足的情况，如果此时要执行一个动作的，需要else语句跟for对齐来写
# 持续提示用户输入一个数字，并对该数字平方运算，如果运算结果小于50，则停止输入


if __name__ == '__main__':
    while True:
        num = float(input('请输入一个数字：'))
        q = num ** 2
        print(f'{num}的平方运算结果是{round(q,2)}')
        if q < 50:
            break


# ---- 总结 -----
# 1、幂次方运算：x ** y
# 2、持续循环：while True: 满足退出条件时用break，否则持续循环。
# 3、round(q,2) 对q四舍五入，保留两位小数
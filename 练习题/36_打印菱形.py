# 定义一个函数，接收一个正整数(奇数)rows，打印一个由*构成的，具有rows行的菱形图案。

# ---------- 我的答案 --------
def draw_lingxing(rows):
    if rows % 2 == 0:
        print('请输入奇数')
    else:
        for i in range(1,rows+1,2):
            blank = int((rows-i)/2)
            print(blank*' '+i*'*')
        for i in range(rows-2,0,-2):
            blank = int((rows - i) / 2)
            print(blank * ' ' + i * '*')

# ---------- 参考答案 --------
def draw_lingxing(rows):
    if rows % 2 == 0:
        print('请输入奇数')
        return

    for i in range(1,rows+1,2):
        blank = int((rows-i)/2)
        print(blank*' '+i*'*')
    for i in range(rows-2,0,-2):
        blank = int((rows - i) / 2)
        print(blank * ' ' + i * '*')


draw_lingxing(11)


# -------- 总结 --------
# 1、函数中的if-else
# 函数中先写异常情况，直接return；
# 再写正常情况的时候，不用else，直接写就可以。



# 1、2、3、4 能组成多少个各不相同且无重复的三位数？分别是多少？

if __name__ == '__main__':
    list = [1,2,3,4]
    num = 0
    for b in list:
        for s in list:
            for g in list:
                if b == s or b == g or s == g:
                    continue
                num += 1
                print(str(b)+str(s)+str(g))
    print(f'各位不重复的三位数共有{num}个')

# -----总结----
# 1、循环嵌套的使用
# 2、统计数据，先定义计数器变量=0
# 3、逻辑运算符and or：也可以用 if b != s and b != g and s != g:
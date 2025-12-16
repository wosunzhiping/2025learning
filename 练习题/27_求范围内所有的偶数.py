# 定义一个函数，用于返回指定范围内所有偶数的列表


# 函数作用：返回指定范围内所有偶数的列表
# 入参：指定范围(x,y)
# 返参：偶数组成的列表list

def list_of_ev(x,y):
    list = []
    for i in range(x,y+1):
        if i % 2 == 0:
            list.append(i)
    return f'{x}到{y}范围内所有的偶数列表是：{list}'


def list_of_ev1(x,y):
    return [i for i in range(x,y+1) if i % 2 == 0]



if __name__ == '__main__':
    print(list_of_ev(1,10))
    print(list_of_ev1(1,10))

# ------总结-------
# 1、列表推导式：
#   [返回值表达式 for 变量 in 可迭代对象 if 条件]
#   [i for i in range(x,y+1) if i % 2 == 0]
# 2、易错点：
#   1）for i in (x,y+1) : 这里i取值只有 x 和 y+1
#   2) for i in range(x,y+1)：这里i才是遍历从x 到 y的所有整数
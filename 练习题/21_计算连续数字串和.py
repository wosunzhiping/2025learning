# 计算a+aa+aaa+aaaa+...的值，其中a是一个数字，由用户决定，且加数的个数也由用户输入决定。

def add_n(a,n):
    if n == 1:
        return a
    return int(str(a)*n) + add_n(a,n-1)



if __name__ == '__main__':
    num = int(input('请输入数字a：'))
    count = int(input('请输入加数个数：'))

    print(f'计算结果是：{add_n(num,count)}')


# ---总结----
# 1、递归函数：
# 当前项包含前一项/后一项，且前一项/后一项的值满足相同的递归关系
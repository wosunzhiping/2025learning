# 定义一个函数，用于返回给定数字列表中所有数字的和


def sum_of_list(list):
    result = 0
    for i in list:
        result += i
    return result

if __name__ == '__main__':
    list1 = [1,2,3,4,5]
    print(f'{list1}所有数字的和是：{sum_of_list(list1)}')

    #直接使用内置函数：
    print(f'{list1}所有数字的和是：{sum(list1)}')


# ------总结-------
# 1、序列各元素求和的内置函数：sum(list)
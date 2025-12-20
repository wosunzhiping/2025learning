# 定义一个函数，接收一个字符串和一个整数作为参数，完成以下操作：
# 1、从字符串头部截取指定数量的字符并翻转；
# 2、从字符串尾部截取相同数量的字符并翻转；
# 3、分别打印头部和尾部翻转后和剩余部分拼接后的新字符串

def head_tail_reverse(str,n):
    head_revers = str[:n][::-1]
    head_remain = str[n:]
    head_result = head_revers + head_remain
    print(f'{str}头部{n}个字符翻转后拼接剩余字符结果是：{head_result}')

    tail_revers = str[-n:][::-1]
    tail_remain = str[:-n]
    tail_result = tail_remain + tail_revers
    print(f'{str}尾部{n}个字符翻转后拼接剩余字符结果是：{tail_result}')

s1 = 'hello,world'
n = 3
head_tail_reverse(s1,n)


# ---------总结-----------
# 1、字符串切片：1）从前往后切：s[0开始的索引且包含:结束索引但不包含:步长] 2）字符串翻转：[::-1] 3）从后往前切：s[-n:]
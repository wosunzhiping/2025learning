# 给定一个整数列表，计算并打印列表中所有偶数的和

if __name__ == '__main__':
    list = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum += i
        else:
            continue
    print(f'列表中所有偶数的和是：{sum}')


# --- 总结 ---
# 1、遍历列表中元素  for i in list
# 2、除法求余数用 % ，除法获取商的整数部分用 //，除法结果四舍五入用 round()
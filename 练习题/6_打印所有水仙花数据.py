# 水仙花数据：指一个三位数，其各位数字立方和等于它本身
import math

if __name__ == '__main__':
    # for i in range(1,10):
    #     for j in range(0,10):
    #         for k in range(0,10):
    #             if i ** 3 + j ** 3 + k ** 3 == int(str(i)+str(j)+str(k)):
    #                 print(int(str(i)+str(j)+str(k)))


# -- 参考答案 ---
    for m in range(100,1000):
        i = m // 100
        # i = math.floor(m/100)
        j = m // 10 % 10
        k = m % 10
        if i ** 3 + j ** 3 + k ** 3 == m:
            print(m)

# -- 总结----
# 1、m // 100 : 除以100后取整
# 2、math.floor(m/100)：也是 除以100后取整
# 3、round(m/100) ：m/100 四舍五入。
#    默认第二个参数是0，即round(m/100,0),表示四舍五入保留0位小数。
# 4、n % 10 : 除以10后取余数
# 5、如何提取整数的各位数字：取整获取前半截数字，取余数获取末尾数据
# 给定圆的半径，定义一个函数，用于返回圆的面积，保留两位小数
import math

def s(r):
    return round(r*r*math.pi,2)

if __name__ == '__main__':
    r = float(input('请输入圆的半径：'))
    print(f'该圆的面积是：{s(r)}')


#--总结---
# 1、math.pi
# 2、round(数字，保留位数)
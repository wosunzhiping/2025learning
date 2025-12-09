# 根据公式：Q=根号(|(2*C*D)/H|),其中C = 50,H = 30,D是从输入序列中以逗号分割出来的数据，计算并打印输出序列，以逗号分割。
import math

def func(x):
    c = 50
    h = 30
    q =  math.floor(math.sqrt(abs(2*c*x/h)))
    return str(q)

if __name__ == '__main__':
    print('请输入一个数据序列：')
    strs = input()
    list = strs.split(',')
    list_res = []
    for i in list:
        list_res.append(func(int(i)))
    print(','.join(list_res))




# -----总结-------
# 1、绝对值：内置函数abs()
# 2、向下取整：math库中的函数，math.floor(xx)
# 3、开根号：math库中的函数，math.sqrt(xxx)
# 4、输出用逗号，分割的字符串：','.join(list)   其中，list中的元素必须是字符串类型
# 5、幂指数：** 运算符，2 ** 3 就是2的3次方的意思
# 6、对输入的数据，以逗号分割，转换成列表： list = input().split(',')
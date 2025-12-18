# 定义一个函数，接收年、月、日作为参数，计算这一天是一年中的第几天

def days_of_feberay(y):
    if y % 4 == 0:
        return 29
    else:
        return 28

def day_of_year(y,m,d):
    if y<=0:
        print('年份输入不正确')
        return None
    if m <= 0 or m > 12:
        print('月份输入不正确')
        return None
    if d <= 0 or d > 31:
        print('日期输入不正确')
        return None

    list = [31,days_of_feberay(y),31,30,31,30,31,31,30,31,30,31]

    # sum = d
    # for i in range(0,m-1):
    #     sum += list[i]
    # return sum

    return sum(list[:m-1])+d


if __name__ == '__main__':
    y = int(input('请输入年份：'))
    m = int(input('请输入月份：'))
    d = int(input('请输入日期：'))
    print(f'{y}年{m}月{d}日是该年的第{day_of_year(y,m,d)}天')


#-------总结---------
# 1、计算某序列前n项和：
#   sum(list[:n])
# 2、如果输入不正确，
#   print错误信息后，
#   要return None，或者仅return ，默认返回None。这样程序到此退出，不会执行之后的判断
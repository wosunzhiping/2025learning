import random
import package

if __name__ == '__main__':
    a = b = c = 100
    a = '你好'
    list = [100,'你好','奇怪']
    str = '最长活到{0[0]}岁,它会说\'{0[1]}\',现在是{0}年'.format(list,2025)



# format 格式化取 字典中的关键字。重点： format(**)
    aninaml1 = {
        'name': "乌龟",
        'age': 100,
        'character': '你好'
    }
    str1 = '{name}最长活到{age}岁，它会说\'{character}\''.format(**aninaml1)
    print(str1)

#输入,format格式化输出百分数
    # add1 = input('请输入除数：')
    # add2 = input('请输入被除数：')
    # print(type(add1))
    # print('{:.2%}'.format(int(add1)/int(add2)))

#进制
    print(bin(1024)) #二进制
    print(oct(1024)) #八进制
    print(hex(1024)) #十六进制



#算数运算符
    a = 9
    b = 4
    c = -4
    print(a/b)
    print(a//b)  #向下取整
    print(a/c)
    print(a//c)  #注意负数的向下取整
    print(a%b)
    print(a**b)  #幂指数

    d,e = divmod(a,b)  #同时计算出商和余数
    print('d:%d,e:%d'%(d,e))

    print(a & b)    #位运算符
    print(a and b)  #逻辑运算符
    print(a | b)    #位运算符
    print(a or b)   #逻辑运算符

    print('## 逻辑运算符AND ###')
    print( False and 20)
    print( 20 and False)
    print( 0 and 20)
    print( 20 and 0)
    print( 10 and 20) #都是真，输出后面的
    print( 20 and 10)
    print( True and 20)
    print( 20 and True)
    print( 1 and 20)
    print( False and False)

    print('## 逻辑运算符OR ###')
    print(10 or 20)
    print(20 or 10) #都为真，输出前面的
    print(10 or 0)
    print(0 or 10) #有一个真，则输出真

    print('## 成员运算符IN ###')
    str = '火柴人'
    list= ['我',1]
    tuple = ('a','b','c')
    dict = {"name":"猪八戒",'age':'30','gender':'male'}
    print('火' in str)
    print(1 in list)
    print('c' in tuple)
    print('age' in dict)
    print('color' in dict)


    print('## 身份运算符ID ###')
    a = 20
    b = 20
    c = a
    print(a == b)
    print(a is b)
    print(id(a)) #内存地址
    print(id(b))
    print(id(c))
    print(id(a) == id(b))

#if,else,while
    # print('#######ifelif###########')
    # num = random.randint(1,100)
    # try:
    #     while True:
    #         initguess = input('请猜这个100以内的正整数是什么？')
    #         if (type(initguess) != int):
    #             initguess = input('输入不合法，请重新输入：')
    #         else:
    #             while (guess != num):
    #             # if(guess not in [1,100]):
    #             if (guess >= 100 or guess <= 0):
    #                 guess = int(input('输入数字非法，请重新输入:'))
    #             if (guess > num):
    #                 guess = int(input('太大了，猜小一点'))
    #             elif (guess < num):
    #                 guess = int(input('太小了，猜大一点'))
    #         if (guess == num):
    #         print('恭喜你猜对了！这个数字是：%d！' % num)
    # except:
    #     print('出现异常，下次再玩')


#while
    i = 1
    sum = 0
    while( i <= 100):
        sum += i
        i += 1
    print('1到100的和是：%d'%sum)

#range()
    print('range(5):')

    for j in range(5):
        print(f'{j}')

    print('range(5,10):')
    for j in range(5,10):
        print(f'{j}')

    print('range(5,15,3)')
    for j in range(5,15,3):
        print(f'{j}')

#案例
    # total = 10000
    # count = 20
    # out = 0
    # balance = total-out
    #
    # for i in range(1,count+1):
    #     score = random.randint(1,10)
    #     if(score<5 and balance > 0):
    #         print(f'序号{i}的员工，绩效是{score},没有领工资')
    #         continue
    #     elif(score >= 5 and balance > 0):
    #         out += 2000
    #         balance = total - out
    #         print(f'序号{i}的员工，绩效是{score},领工资2000，当前余额{balance}')
    #     elif(balance <= 0):
    #         print(f'到序号为{i}的员工，已经没有工资可领了')
    #         break


#列表
    list_name =  ['花1','花2','花3']
    del list_name[1]
    print(list_name)
    rs = list_name.pop(1)
    print(list_name)
    print(rs)

    list_int = [21,25,21,23,22,20]
    list_int.append(31)
    list_int2 = [29,33,30]
    list_int.extend(list_int2)
    print(f'第一个元素是{list_int[0]}')
    print(f'最后一个元素是{list_int[-1]}')
    print(f'最后一个元素是{list_int[len(list_int)-1]}')
    print(f'元素31在列表中的下标是{list_int.index(31)}')

    i = 0
    while i in range(len(list_int)):
        print(list_int[i])
        i += 1

    print('-----for--1---')
    for i in range(len(list_int)):
        print(list_int[i])
        i += 1
    print('-----for--2---')
    for x in list_int:
        print(x)
        i += 1

# 列表联系
    list_init = [1,2,3,4,5,6,7,8,9,10]
    list_ou = []

    for x in list_init:
        if x%2 == 0:
            list_ou.append(x)
    print(list_ou)

    print('----while-ou----')

    i = 0
    list_ou_2 = []
    while i in range(len(list_init)):
        if list_init[i]%2 ==  0:
            list_ou_2.append(list_init[i])
        i += 1
    print(list_ou_2)











import functools
import builtins

if __name__ == '__main__':

#默认参数，位置参数
    print('-----默认参数，位置参数-----')
    def funa(a,b=1):
        return b
    print(funa(2,3))

#可变参数
    print('----可变参数，一个*，元组-----')
    def funb(*args):
        return args
    print(funb())
    print(funb(1))
    print(funb(1,2))
    print(funb(1,2,'哈哈'))

#关键字参数
    print('-----关键字参数，俩*，字典-----')
    def func(**kwargs):
        return kwargs
    print(func())
    # print(func(1))
    print(func(name = '孙悟空',home = '花果山'))

#作用域
    print('-----变量作用域，global，nonlocal-----')
    a = 100
    b = 200
    def fund():
        print(f'a的地址是{id(a)},a的值是{a}')
        print(f'b的地址是{id(b)},a的值是{b}')
    def fune():
        a = 120
        global b
        b = 250
        print(f'a的地址是{id(a)},a的值是{a}')
        print(f'b的地址是{id(b)},a的值是{b}')
    fund()
    fune()
    print(f'a的地址是{id(a)},a的值是{a}')
    print(f'a的地址是{id(b)},a的值是{b}')

    def fun_out():
        c = 300
        print(f'fun_out中的c是{c}')
        def fun_inner():
            nonlocal c
            c = 400
            print(f'fun_inner中的c是{c}')
        fun_inner()
        print(f'此时fun_out中的c是{c}')
    fun_out()

#匿名函数lambda
    print('-----匿名函数lambda------')
    add = lambda a,b:a+b
    print(add(1,4))

    print('------三目运算符-------')
    a = 5
    b = 4
    print('a<b' if a<b else 'a>=b')

    comp = lambda a,b:'a>b' if a>b else 'a<=b'

#内置函数
    print('-------所有的内置函数--------')
    print(dir(builtins))
    print('-----zip函数:两个列表元素一一对应------')
    names = ['huahua','lele']
    ages = [25,30]
    print(type(zip(names,ages)))
    print(zip(names,ages))
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")
    print('\n')
    for name,age in zip(names,ages):
        print(f"{name}:{age}")
    print('\n')
    print(list(zip(names,ages)))

    print('--------zip函数：两个列表合并成字典键值对-----')
    key = ['name','age','gender']
    value = ['huahua',18,'female']
    dictionary = dict(zip(key,value))
    print(dictionary)
    print(dictionary)

    print('-------map函数，把列表中的元素每个都带入函数执行一次----------')
    funf = lambda a:a*2
    list1 = [2,4,6]
    mp = map(funf,list1)
    print(type(mp))
    print(mp)
    print(list(mp))
    print(mp)
    print(list(mp))
    print('--mp是一个迭代器，被取出后，内部指针会留在尾部，再访问就是空---')

    print('-----------reduce函数，依次操作序列里相邻两个元素（其使用的函数必须有且只有两个变量）------')
    fung = lambda a,b:(a+b)*2
    list2 = [1,2,3,4,5,6]
    res = functools.reduce(fung,list2)
    print(res)


    print('-------拆包-------')
    tup= (1,2,3,'a','b','c')
    a,*b = tup
    print(a,b)
    c,d,e, *f = b
    print(c,d,e,f)

    list1 = [4,5,6,'A','B','C']
    a,b,c,*d = list1
    print(a,b,c,d)
    print(type(d))


    def funk(a,b,*args):
        print(a,b)
        print(args,'\n',type(args))
    funk(1,2,3,4,5,6)
    funk(*list1)






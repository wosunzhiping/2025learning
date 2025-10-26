
# 递归
print('-------递归---------')
def add(n):
    if n==1:
        return 1 #有明确的结束条件
    return n+add(n-1)  #自己调用自己
print(add(100))



# 1,1,2,3,5,8,13

def funa(n):
    if n == 0 or n == 1:
        return 1
    return funa(n-2)+funa(n-1)
print(funa(6))



print('-----闭包------')
def outer(m):
    n = 2
    print('这是外部函数，其参数是m:%d，局部变量是n:%d'%(m,n))
    def inner(o):
        p = 3
        print('这是内部函数，其参数是o:%d,其局部变量是p:%d,其使用的外部函数局部变量是n:%d,其使用的外部函数的参数是m:%d'%(o,p,m,n))
    return inner
ou = outer(1)
ou(10)
ou(11) # 虽然outer外部函数只调用了一次，后面多次仅调用内部函数，使用的仍然是最开始外部函数中的变量及局部变量


print('------装饰器-------')
def outz(fn):
    print('outtz的外层函数被调用')
    def innerz(name):
        print('outtz的内层函数被',fn(name),'调用')
    return innerz
@outz
def send(name):
    print(f'这是被装饰的函数send,形参是\'{name}\'') #被装饰的函数有参数的话，引用了它的内函数也要有同名函数作为参数
    return f'{name}'
send('哈哈')


print('------装饰器,可变入参-------')
def outzb(fn):
    print('outzb的外层函数被调用')
    def innerzb(*args,**kwargs):
        print('outzb的内层函数被',fn(*args,**kwargs),'调用')
        print('outzb的内层函数被',fn(),'调用')
        print('outzb的内层函数被调用')

        # fn(*args,**kwargs)
    return innerzb

def outzc(fn):
    print('outzc的外层函数被调用')
    def innerzc(*args,**kwargs):
        print('outzc的内层函数被',fn(*args,**kwargs),'调用')
    return innerzc

@outzb
def func(*args,**kwargs):
    print(f'这是被装饰的函数func,形参是{args},{kwargs}')
    return (f'{args},{kwargs}')
func('哈哈','lele',name='lele')



print('--------两个装饰器-----------')
def bb1(fn):
    def inner_bb1():
        return '哈哈哈'+fn()+'呵呵呵'
    return inner_bb1

def bb2(fn):
    def inner_bb2():
        return '嘻嘻嘻'+fn()+'嘿嘿嘿'
    return inner_bb2

@bb1 #此语法糖出现，意思是执行该bb1闭包外函数，及其内函数，内函数执行前，先执行被装饰的函数，将其返回值带入内函数去执行内函数
@bb2
def test():
    return '我在测试'

print(test())



def pre(fn):  # 外层函数有且只有一个形参，且为函数类型
    print('pre被执行')
    def inner(): #内部定义内部函数，实现部分功能的同时，调用了外部函数中的函数形参
        print('先验证登录态')
        fn()
    return inner #返回内部函数名


@pre  #使用装饰器语法糖，其作用是在 commit() 执行之前，先执行 pre函数，并且完成对commit的偷梁换柱
def commit():
    print('提交操作')

commit()

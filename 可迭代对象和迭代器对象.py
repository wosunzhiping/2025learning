from collections.abc import Iterable,Iterator

print('-----可迭代对象(Iterable),迭代器(Iterator),isinstance-------')
'''
先导入: from  collections.abc import Iterable
可用于for循环中循环读取的对象
'''
# r1 = isinstance('123',(int,str))  #判断一个对象是否是某种数据类型
# r2 = isinstance('123',Iterable)   #判断一个对象是否是可迭代对象
# print(r1,r2)
# for i in 'abc':
#     print(i)


print('-------可迭代对象的迭代取值逻辑：_iter__(),__next__()--------')
# list1 = [1,2,3,4,'a','b','c']
# for i in list1:
#     print(i)

print('------创建迭代器对象:iter(可迭代对象Iterable),next(迭代器对象Iterator); 或者可迭代对象.__iter__(),迭代器对象.__next__()-------')

'''可迭代对象转换为迭代器对象：方式一'''
# list1 = [1,2,3,4,'a','b','c']
# l1 = iter(list1)  #创建/转换为迭代器对象 -- l1 = list1.iter()  # 书写错误
# r1 = isinstance(l1,Iterable)
# r2 = isinstance(l1,Iterator)
# r3 = isinstance(list1,Iterable)
# r4 = isinstance(list1,Iterator)
# print(r1,r2,r3,r4)
# print('list1 %s 可迭代对象，list1 %s 迭代器'%(isinstance(list1,Iterable),isinstance(list1,Iterator)))
# print('l1 %s 可迭代对象，l1 %s 迭代器'%(isinstance(l1,Iterable),isinstance(l1,Iterator)))
# print(l1)
# '''Iterable的使用'''
# for i in list1:
#     print(i)
# '''Iterator的使用1'''
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# '''Iterator的使用2'''
# for i in l1:
#     print(i)



'''可迭代对象转换为迭代器对象：方式二'''
# list1 = [1,2,3,4,'a','b','c']
# l2 = list1.__iter__()  #创建/转换为迭代器对象
# print(l2)
# print(l2.__next__())
# print(l2.__next__())
# print(l2.__next__())
# print(l2.__next__())
# print(l2.__next__())
# print(l2.__next__())
# print(l2.__next__())
#
#

'''迭代器对象，一定是可迭代对象(迭代器对象是可迭代对象的子集)；可迭代对象有__iter__()方法，迭代器对象同时拥有__iter__()和__next__()方法'''



print('--------自定义迭代器类，需要有两个方法，__iter__(self)和__next__(self)----------')
# class Myiterator:
#     def __init__(self,num):
#         self.num = num
#     def __iter__(self):
#         return self      #如果没有这个__iter__(self)方法，这个类就不是一个Itrable对象，就不可迭代
#     def __next__(self):
#         # print(self.num)
#         self.num += 1
#         if self.num == 9:
#             raise StopIteration("终止迭代")
#         return self.num
# mi = Myiterator(0)
# print(mi)
# print(isinstance(mi,Iterable))
# print(mi.num)

# for i in mi:  #在for循环中，mi 就在执行自己的__next__()函数了
#     print(i)


print('---------------生成器：生成器表达式-----------------------')
# li = [i*4 for i in range(5)]  #列表推导式
# print(li)
#
#
# gen = (i*4 for i in range(5)) #生成器表达式,这样赋值的是一个生成器对象
# print(gen)
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# for i in gen:
#     print(i)







print('---------------生成器函数：用yield语句实现的迭代器，简化迭代器的创建-----------------------')
# def mygener(num):  #这是一个方法，但是调用这个方法得到的是一个生成器对象(迭代器对象的一种)
#     while num<10:
#         yield num   #yield类似return，将指定值返回给调用者；一次只返回一个结果，下次再执行时从中断的地方继续往后
#         num += 1
# gen = mygener(0)
# print(gen)  #这是一个generator对象
# print(isinstance(mygener(0),Iterator))
#
# for i in mygener(0):
#     print(i)



# def gen():
#     yield 'a'
#     yield 'b'
#     yield 'c'
# gen_01 = gen()
# print(next(gen_01))  #生成器对象，用next方法取数，一次只返回一个yield后面的内容，暂停并挂起函数，多次执行时，从上次中断的地方继续
# print(next(gen_01))
# print(next(gen_01))
# print(next(gen_01))


def gen2(n):
    li = []
    for i in range(n):
        li.append(i)
        print('li里面:', li)
        yield i   # yield在哪，在后面使用的时候循环中函数就在哪里挂起然后再执行下一次循环
    print("li最后：",li)


for i in gen2(5):
    print(i)

# print(next(gen2(5)))


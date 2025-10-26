print('--------类中的方法：self是类中的方法必须具备的形参，初始化函数-----')
class Person:
    arms = 2
    def __init__(self,name,age):  #初始化函数,是在创建对象的时候立刻执行的函数，用于传递具体的实例属性进来
        self.name = name
        self.age = age   #实例属性，非类属性

    def play(self):      #有self，是实例方法
        print(f'{self.name}在玩游戏')

    def __del__(self):
        print('这是一个析构函数')

#pe1 = Person()
#pe1.age = 20
#print(pe1.arms)
#print(pe1.age)
pe2 = Person('mingming',20)
pe2.play()
del pe2

print('-----析构函数-------')  #当程序块执行结束的时候，或者主动删除实例对象的时候，解释器调用析构函数
pe3 = Person('huahua',18)
pe3.play()



print('------封装-面向对象的三大特性之一，私有属性-------')
class Cat:
    name = 'lele'  #类属性
    _color = 'yellow' #受保护的属性
    __age = 20     #私有类属性
    def introduce(self):
        print(f'{self.name}的年纪是{self.__age}') #在类的内部，可以访问类的私有属性
        print(f'{Cat.name}的年纪是{Cat.__age}')
ca = Cat()
print(ca.name)
print(ca._color)
#print(ca.__age) #报错，无法访问
print(ca._Cat__age)  #通过这种方式可以访问类的私有属性，但是不推荐

print('-----封装之--在类的内部访问和修改私有属性----')
ca.introduce()

class Employee:
    def __init__(self,name,sal):
        self._name = name
        self.__sal = sal
e1 = Employee("牛马",2000)
print(e1._name)
print(e1._Employee__sal)


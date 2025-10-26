print('-----单继承-基础继承 和 多态 --------')
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def introduce(self):
        print(f'{self.name}的颜色是{self.color}')
    def bite(self):
        print(f'{self.name}会咬人')

class Cat(Animal):     #子类名(父类名) 就是继承，父类中所有的非私有的属性和方法；----继承
    pass   #占位符

class Dog(Animal):     #有不同于父类的属性或方法，就叫----派生类
    def bite(self):
        print(f'{name}会咬人')
    def introduce(self):    #父类方法（同名方法）------重写
        print(f'{self.name}是一只{self.color}的狗')

class Bird(Animal):
    def __init__(self,name,color):
        self.name = color
        self.color = name

    def introduce(self):    #父类的同名方法在不同的子类中被重写成不同的方法，就叫----多态
        print(f'{self.name}是鸟的形态,颜色是{self.color}')

cat1 = Animal('喵喵','white')
dog1 = Animal('大黄','yellow')
cat1.introduce()
dog1.introduce()

print('-----多态性-----')
def test(obj):           #定义一个接口，形参为对象，传入不同的对象，执行不同对象的同名方法
    obj.introduce()

cat2 = Cat('小花','灰色')  #子类继承了父类的构造方法，所以实例化的时候传参方式与父类实例化传参方式一致
dog2 = Dog('旺财','黑色')     #但是子类不能继承除了父类构造方法以外的其他父类的私有方法
bird2 = Bird('学舌','虎皮')


test(cat2)
test(dog2)
test(bird2)


print('------子类方法在父类方法基础上扩展-------')
class Mouse(Animal):
    def introduce(self):
        print(f'这是一只老鼠')
        Animal.bite(self)

mouse1 = Mouse("吱吱","灰色")
mouse1.introduce()


print('------新式类--------')
print(dir(object))  #python3中，所有的类都默认继承object类，无需显式声明，也叫---新式类；object有内置属性和方法
print(dir(Cat))



print('--------多继承-----------')
class Father:
    def __init__(self,sex):
        self.sex = sex
        print(f'我是{self.sex}爸爸')
    def money(self):
        print('我有100万可被继承')
class Mother:
    def __init__(self,height):
        self.height = height
    def apparence(self):
        print(f'身高{self.height}会影响继承的个头')
    def money(self):
        print('我有10万可被继承')

class Son(Father,Mother):
    pass

son1 = Son('男')
#son2 = Son()     报错，因为缺少Father构造函数中的入参
son1.money()
print(Son.__mro__)   #__mro__展示类的方法的搜索顺序：多继承时，如多个父类中有同名函数，按继承顺序先使用前面父类中的函数




print('-----静态方法，类方法-----')
class Car:
    region = '亚洲'
    @staticmethod
    def run():      #静态方法：这里不需要self做为必备的形参
        print('这是Car类里定义的静态方法')

    @staticmethod
    def stay(name):  #静态方法：无法访问类属性或实例属性
        print(f'{name}趴窝了')

    @classmethod
    def sleep(cls):
        print(f'{cls.region}的会睡觉')  #类方法：可以访问类属性

Car.run()
Car.stay('奇瑞')
Car.sleep()


print('-------单例模式--------')
class Singlemode:
    obj = None
    @classmethod  # 可写可不写
    def __new__(cls, *args, **kwargs):
        print('1、先执行基类object的__new__方法,这里把该方法重写，其中用到了扩展基类同名方法的写法super().xxx')
        if cls.obj == None :
            return super().__new__(cls)    #__new__方法的作用：1，创建类的实例；2，返回实例的地址
        return cls.obj
    def __init__(self,name):
        self.name = name
        print(f'2、执行完__new__方法后执行__init__方法，传参是{self.name}')

s1 = Singlemode('s1')
print(s1)
s2 = Singlemode('s2')
print(s2)


print('------魔法方法-----')
class A:
    def __call__(self, *args, **kwargs):
        print('回调方法')
a1 = A()
a2 = A()
a1()
a2()
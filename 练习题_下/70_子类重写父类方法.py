# 1、定义一个父类 Vehicle ，包含一个方法 describe ,用于描述车辆的基本信息
# 2、定义一个子类 Car，继承自Vehicle，并重写describe 方法，以提供关于汽车的特定信息

class Vehicle:
    def __init__(self,made,model):
        self.made = made
        self.model = model
    def describe(self):
        print(f'父类基本信息：车辆产自{self.made},型号是{self.model}')

class Car(Vehicle):
    def __init__(self,made,model,year):
        super().__init__(made,model)
        self.year = year
    def describe(self):
        print(f'汽车基本信息：车辆产自{self.made},型号是{self.model}，年份{self.year}')

car = Car('china','volvo',2025)
car.describe()


# ----- 总结 ------
# 1、子类继承父类的写法：
# 父类名放到括号内-- class Car(Vehicle):

# 2、构造方法：
# 1）子类的构造方法如果写了，就会覆盖父类的构造方法
# 2）子类的构造方法中继承父类构造方法，要用super().__init__(made,model),
# 注意super后有();
# 并且参数中不需要再有self了
#
# 3、子类中重写父类方法。
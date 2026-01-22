# 定义一个简单的银行账户类，支持存款和取款

class Account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print(f'存入成功，当前余额{self.balance}')
        else:
            print('存入金额必须为正数!')
        return self.balance

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'取出成功，当前余额{self.balance}')
        else:
            print('不支持取出操作！')

a = Account('a',100)
a.deposite(2)
a.deposite(8)
a.withdraw(3)

# ---- 总结 ------
# 1、类中的实例属性：
# 1）如果不同的实例它们的属性值会不一样，就要定义实例属性
# 2）实例属性定义在构造方法__init__里，并通过参数传入

# 2、类的实例属性中有owner了，即定义实例属性的时候就明确了是哪个owner，
# 后续的存钱和取钱方法，都是基于这个对象的(owner属性已经是确定的了，可以直接拿来用的)，所以方法的入参中无需再传入owner

# 3、类的实例属性中有balance，
# 当这个类的一个对象生成后没有消失，
# 那么它的所有方法对这个参数的操作后的结果都会保留下来，后面的操作都会基于前面操作后的结果继续
#
# 2、默认参数：def __init__(self,owner,balance = 0)
# 如果传了两个参数，那么第二个参数就是balance的值，
# 如果不传，则balance使用默认值0


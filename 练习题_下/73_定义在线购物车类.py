# 定义一个在线购物车类，支持添加、删除商品、查看购物车内容以及计算总价

class Cart:
    def __init__(self):
        self.goods = {}  # 键是商品，值是字典 -- 数量和单价的字典

    def add_goods(self,name,amount=0,price=0):
        if name in self.goods:
            self.goods[name]['quatity'] += amount
        else:
            self.goods[name] = {'quatity':amount,'price':price}  # 值是字典的新建方法

    def delete_goods(self,name,amount=None):
        if name not in self.goods:
            print(f'购物车中不存在商品{name}，无法删除')
        elif name in self.goods and amount != None and self.goods[name]['quatity']>=amount>0 :
            self.goods[name]['quatity'] -= amount
        elif name in self.goods and amount != None and self.goods[name]['quatity']<amount:
            print(f'数量超出购物车中已有数量，无法删除')
        elif name in self.goods and amount == None:  # 或者 amount is None
            del self.goods[name]


    def view_cart(self):
        for name,dic in self.goods.items():
            # print(f'{name}单价是{list(dic.keys())[0]},数量是{list(dic.values())[0]}')
            print(f"{name}单价是{dic['price']},数量是{dic['quatity']}") # 单引号和双引号


    def total_cost(self):
        sum = 0
        for dic in self.goods.values():
           sum += dic['quatity'] * dic['price']
        return sum

my_shopping = Cart()
my_shopping.add_goods('苹果',5,5)
my_shopping.add_goods('泡面',5,25)
my_shopping.add_goods('火腿肠',5,15)
# my_shopping.view_cart()
my_shopping.delete_goods('泡面',2)
# my_shopping.view_cart()

my_shopping.delete_goods('苹果')
my_shopping.view_cart()
print(f'购物车商品总价：{my_shopping.total_cost()}')


# ------ 总结 -------
# 1、嵌套字典：字典中的值也是字典，值的字典中的key要明确，这样才好后续操作
# 1）新增键值对：self.goods[name] = {'quatity':amount,'price':price}
# 2）访问值中的一个键：self.goods[name]['quatity']
#
# 2、为空的判断写法：
# amount == None
# 或者 amount is None
#
# 3、f表达式中
# 如果引用的内容含有单引号，则f表达式用双引号
# print(f"{name}单价是{dic['price']},数量是{dic['quatity']}")
#
# 4、提取字典中的某个key值：
# 先转为list，然后按索引获取
# list(dic.keys())[0]
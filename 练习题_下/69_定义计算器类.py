# 定义一个简单的计算器类，支持加减乘除四个运算

class Caculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y
    def multiplicate(self):
        return self.x * self.y
    def division(self):
        if self.y == 0:
            raise Exception('分母不能为0')
        return self.x / self.y

calculate = Caculator(1,0)
try:
    print(calculate.add(),calculate.subtract(),calculate.multiplicate(),calculate.division())
except Exception as e:
    print(e)


# ----- 总结 ---------
# 1、在函数中自定义异常：
# raise Exception('异常告警文字描述')
# 2、捕获异常使用：
# except Exception as e:
#   print(e)
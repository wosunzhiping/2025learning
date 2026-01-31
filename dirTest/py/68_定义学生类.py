# 定义一个学生类，用于存储学生的基本信息：姓名、年龄、学号；并提供查询这些信息的方法

class Student:
    def __init__(self,name,age,number):
        self.name = name
        self.age = age
        self.number = number


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_number(self):
        return self.number


student1 = Student('花花',18,10)

print(student1.get_name(),student1.get_age(),student1.get_number())



# ------- 总结 ---------
# 1、类的定义：
# 1）类名首字母大写
# 2）首先定义初始化方法，参数在初始化方法入参中传入
# 3）类的实例化，类名(初始化函数中的参数)



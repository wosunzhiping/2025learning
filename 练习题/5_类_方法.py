# 定一个有两个方法的类，一个获取输入的字符串，一个将字符串中的小写字母转换成大写并打印。

class ptest:
#-------------我的答案（错误）---------------
    # def __init__(self):
    #     print('请输入字符串：')
    # def getString(self):
    #     print('请输入字符串：')
    #     return input()
    #
    # def printString(self):
    #     print(self.getString().upper())


#-------------参考答案----------------
    def __init__(self):
        self.s = ''

    def getString(self):
        print('请输入字符串：')
        self.s = input()

    def printString(self):
        print(self.s.upper())

if __name__ == '__main__':
    p = ptest()
    p.getString()
    p.printString()


# 总结：
# 1、class ptest(object) ，python3 中并不需要显示的继承object类，默认全部继承object类，直接写成class ptest: 即可
# 2、所有方法中函数均有形参 self
# 3、可以通过__init__中定义的初始化类的属性，在多个类的函数间传递信息。
# 4、创建实例：p = ptest()
# 这个系统允许我们添加学生、记录学生成绩，并计算每个学生的平均成绩


class Student:
    def __init__(self,name):
        self.name = name
        self.StudentScoreList = {'语文':0,'数学':0,'英语':0}


    def add_score(self,chinese=0,math=0,english=0):  # 默认值参数  #这里添加成绩，不需要传入name了
        self.StudentScoreList['语文'] = chinese
        self.StudentScoreList['数学'] = math
        self.StudentScoreList['英语'] = english


    def average_score(self):
        return (self.StudentScoreList['语文'] + self.StudentScoreList['数学'] + self.StudentScoreList['英语'])/3



class StudentManage:
    def __init__(self):
        self.students = {}

    def add_student(self,name):
        if name not in self.students:  # 键不存在字典中
            self.students[name] = Student(name)  # 给字典添加键值对，值是一个类的实例对象，这个对象有自己的属性name和成绩字典，这是一个整体，不是一个复合字典
        else:
            print(f'{name}已存在')

    def get_student(self,name):
        return self.students.get(name)  # 字典中查找某个key对应的value，这里返回的是student对象。

    def add_grade_to_student(self,name,chinese=0,math=0,english=0):
        student = self.get_student(name) # 返回的是student对象
        if student:
            student.add_score(chinese,math,english)
        else:
            print(f'{name}不存在')

    def show_average_score(self):
        for name,student in self.students.items():  # 解包获取字典中的键和值
            print(f'{name}的平均成绩是{student.average_score():.1f}')



student_zs = Student('张三')
student_ls = Student('李四')

student_zs.add_score(98,99,100)

print(student_zs.average_score())
print(student_ls.average_score())

manager = StudentManage()
manager.add_student('张三')
manager.add_student('李四')
manager.add_student('王五')
manager.add_grade_to_student('张三',80,90,23)
manager.show_average_score()


dic1 = {'a':1,'b':2}
print(dic1.get('c'))



# ------ 总结 --------
# 1、概念重塑：
# 学生管理类的对象，它只有一个实例属性：一个字典，所以可以简单理解为学生管理类的对象就是一个字典；它还有几个可以调用的方法
# 而学生类的对象，它有两个实例属性：一个name，和一个字典。
#   所以，学生管理类对象不是一个简单的字典，
#   它作为学生管理类的字典中的值的时候，就是一个包裹，它可以有name和分数字典两个属性，还有可以调用的方法

# 2、明确类的作用，帮助明确类中方法的写法：
# 学生类，是管理单独一个学生的成绩的，所以name在初始化时就做为类的对象的实例属性了，
# 其余方法如果用到name，直接使用即可，无需再作为参数传入


# 3、定义方法中使用默认值参数：
# def add_score(self,chinese=0,math=0,english=0):
# 如果传参有数字，则使用传入的数字，没有传，则使用默认值

# 4、条件语句 如果列表不为空 的写法：
# if not list:



# 字典中的一些操作：
# 5、条件语句 如果键不存在在字典中：
# if name not in self.students

# 6、给字典添加键值对，值是一个类的实例对象，这个对象有自己的属性name和成绩字典，这是一个整体，不是一个复合字典
# self.students[name] = Student(name)

# 7、获取字典某个键的值：
# 用dic1.get(键)，如果键不存在，返回None，不会报错
# 如果直接用 self.students[name] 获取，如果name不存在会报错

# 8、解包获取 和 使用 字典中的键和值：
# for name,student in self.students.items():
# print(f'{name}的平均成绩是{student.average_score():.2f}')





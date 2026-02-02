# 从 course_teacher.txt 和 grade.txt 两个文件中读取信息，打印出包含课程名称、教师姓名、学生学号、学生姓名、学生成绩的完整信息


# ------ 我的答案 -------
# course_teacher = {}
# with open('course_teacher.txt',encoding='utf-8') as f:
#     for line in f.readlines():
#         line = line.replace('\n','').split('，')
#         if line[0] not in course_teacher:
#             course_teacher[line[0]] = ''
#         course_teacher[line[0]] = line[1]
# # print(course_teacher)
#
# with open('grade.txt','r',encoding='utf-8') as f:
#     for line in f.readlines():
#         line = line.replace('\n','').replace('  ','').split(',')
#         line.insert(1,course_teacher[line[0]])
#         print(line)


# -------- 参考答案 --------
course_teacher = {}
with open('course_teacher.txt',encoding='utf-8') as f:
    for line in f.readlines():
        course,teacher = line.replace('\n','').split("，")
        course_teacher[course] = teacher

with open('grade.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        course,sid,name,grade = line.replace('\n','').split(",")
        teacher = course_teacher.get(course)
        print(course,teacher,sid,name,grade)



# ------ 总结 -----------
# 1、获取字典中某键的值：
# 用dic.get(键)
# 不用dic[键]，
# 因为如果键在字典中不存在的化，第一种方法会返回none不会报错，第二种方法会报错，程序会终止

# 2、列表的解包：
# course,teacher = line.replace('\n','').split("，")
# course,sid,name,grade = line.replace('\n','').split(",")

# 3、关联数据获取方式：
# 用字典的键值对，获取所需要的键对应的值





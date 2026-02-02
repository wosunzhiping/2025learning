# 从grade.txt文件中读取课程和学生成绩信息，并打印出每门课程的最高分、最低分、平均分


import os


# ------ 我的答案 -------------

# course_grade = {}
# with open('grade.txt','r',encoding='utf-8') as f:
#     for line in f.readlines():
#         line = line.replace('\n','').replace('  ','').split(',')
#         if line[0] not in course_grade:
#             course_grade[line[0]] = []
#         course_grade[line[0]].append(int(line[3]))
# print(course_grade)
#
# for course,grades in course_grade.items():
#     print(f'学科：{course}，最高分:{max(grades)}，最低分：{min(grades)}，平均分：{sum(grades)/len(grades):.2f}')



# ------ 参考答案的差异点 -------------

course_grades = {}
with open('grade.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.replace('\n','').replace('  ','').split(',')
        course , sid , name , grade = line
        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(grade)

print(course_grades)





# ------ 总结 --------
# 1、简化写法：
# 如果成绩不存在于字典中，则创建该成绩及空列表的键值对，并给值添加一个值，如果成绩存在，则只添加值。
# if line[0] not in course_grade:
#     course_grade[line[0]] = []
# course_grade[line[0]].append(int(line[3]))
# 无需写完if再写else，因为都需要执行在值的列表中添加元素的动作

# 2、列表的解包：
# line = line.replace('\n','').replace('  ','').split(',')
# course , sid , name , grade = line
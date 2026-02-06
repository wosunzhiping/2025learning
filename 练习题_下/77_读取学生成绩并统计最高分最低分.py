# 从 student_grade_file.txt 文件中读取学生成绩，并计算最高分、最低分、平均分(保留两位小数)

# ------- 我的答案 ----------

# def read_file():
#     result = []
#     with open('student_grade_file.txt','r',encoding='utf-8') as f:
#         for line in f.readlines():
#             line = line.replace('\n','')
#             line = line.split('，')
#             result.append(line)
#         return result
#
# def m_grade(lst,type):
#     sorted_grade = sorted(lst,key=lambda x:x[2],reverse=True)
#     if type == 'max':
#         return sorted_grade[0]
#     elif type == 'min':
#         return sorted_grade[-1]
#     else:
#         return '入参不正确，请检查'
#
# def average(lst):
#     sum = 0
#     for line in lst:
#         sum += int(line[2])
#     return f'{(sum/len(lst)):.2f}'
#
#
# print(read_file())
# lst = read_file()
# print(m_grade(lst,'max'))
# print(m_grade(lst,'in'))
# print(average(lst))


# ----- 参考答案 ----------

def compute_scores():
    scores = []
    with open('student_grade_file.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            line = line.split('，')
            scores.append(float(line[2]))
        return max(scores),min(scores),sum(scores)/len(scores)

max_score,min_score,average_score = compute_scores()

print(f'最高分：{max_score}，最低分：{min_score}，平均分：{average_score:.2f}')



# ------- 总结 --------
# 1、文件读取：
# 按行读到字符串，并生成列表
#         for line in f.readlines():
#             line = line.replace('\n', '')
#             line = line.split('，')

# 2、return 一次性返回多个值，自动组成元组返回
# return max(scores),min(scores),sum(scores)/len(scores)

# 3、接收并解包元组：
# max_score,min_score,average_score = compute_scores()

# 4、保留两位小数：在f''输出中，在数值后面:.2f
# 平均分：{average_score:.2f}'



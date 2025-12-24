# 编写一个程序，可以根据用户指定的长度，随机生成一个验证码（含大小写英文字母及数字）
import random
import string


# ------------我的答案 ---------------
# def create_verification(n):
#     code = ''
#     candidate_letter = list(string.ascii_letters)
#     candidate_number = ['0','1','2','3','4','5','6','7','8','9']
#     candidate = candidate_letter + candidate_number
#     for i in range(0,n):
#         code += random.choice(candidate)
#     return code


# --------参考答案---------------
def create_verification(n):
    code = ''
    candidate = string.ascii_letters + string.digits
    print(string.ascii_letters)
    print(string.digits)
    for i in range(0, n):
        code += random.choice(candidate)
    return code

n = int(input('请输入验证码的位数：'))
print(create_verification(n))


# -------- 总结 --------
# 1、import string
#    所有英文字母组成的字符串：string.ascii_letters
#    所有大写英文字母组成的字符串：string.ascii_uppercase
#    所有小写英文字母组成的字符串：string.ascii_lowercase
#    所有数字组成的字符串：string.digits
# 2、字符串转成列表：list(string.digits)
# 3、循环10次，可以直接写 ： for i in range(10)
# 4、在指定范围内生成一个随机项,入参是个序列，可以是字符串、列表或其他序列：random.choice(candidate)

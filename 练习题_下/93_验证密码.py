# 定义一个函数，验证密码是否符合规范
# 1. 长度位于 6 - 20 之间
# 2. 必须包含至少 1 个小写字母
# 3. 必须包含至少 1 个大写字母
# 4. 必须包含至少 1 个数字
# 5. 必须包含至少 1 个特殊字符

import re


# ---- 我的答案1 ---------

# def check_pwd(pwd):
#     if 6<=len(pwd)<=20 and re.search('[a-z]+',pwd) and re.search('[A-Z]+',pwd) and re.search('\d+',pwd) and re.search(r'[^a-zA-Z0-9]',pwd):
#         print('验证通过')
#     else:
#         print('密码错误')



# ----- 我的答案2 ---------
def check_pwd_2(pwd):
    if not 6<=len(pwd)<=20 :
        return False,'长度需位于 6 - 20 之间'
    if re.search('[a-z]+',pwd) == None:
        return False, '必须包含至少 1 个小写字母'

    if re.search('[A-Z]+',pwd) == None:
        return False, '必须包含至少 1 个大写字母'
    if re.search('\d+',pwd) == None:
        return False, '必须包含至少 1 个数字'
    if re.search(r'[^a-zA-Z0-9]',pwd) == None:
        return False, '必须包含至少 1 个特殊字符'

    return True,'验证通过'


pwd = '1Q$1134'

print(check_pwd_2(pwd))


# ------- 总结 ---------
# 1、if not 的使用：
#     if not 6<=len(pwd)<=20 :
# 2、return 后面写两个内容，是组成一个元组返回：
#         return False,'长度需位于 6 - 20 之间'
# 3、特殊字符：
# r'[^a-zA-Z0-9]',
# r'\W'
# 1）注意表达式字符串前面写r
# 4、注意这种不合规的原因要逐个写出并return，最后就是合规返回成功的写法

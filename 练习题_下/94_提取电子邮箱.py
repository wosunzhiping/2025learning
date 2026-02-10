# 给定一段含有多个邮箱地址的文本，提取所有标准的邮箱地址

import re

content = '''
寻隐者12345@qq.com不遇
朝代：唐asdf12dsa#abc.com代
作者：贾岛
松下问童子，言师python666@163.cn采药去。
只在python_ant-666@sina.net此山中，云深不知处。'''



pattern = re.compile('''
[0-9a-zA-Z_-]+
@
[0-9a-zA-Z]+
\.
[a-z]{2,4}
''',re.VERBOSE)

res = re.findall(pattern,content)
print(res)



# --------- 总结 ----------
# 1、编译生成正则表达式：
#   re.compile('''这中间可以换行''',re.VERBOSE)
#
#
# [0-9a-zA-Z_-]+       至少一个数字或小写字母或大写字母
# @
# [0-9a-zA-Z]+
# \.                   匹配点，要加\
# [a-z]{2,4}


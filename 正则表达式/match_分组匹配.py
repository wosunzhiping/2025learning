import re

if __name__ == '__main__':
    res = re.match('[a-zA-Z][a-zA-Z]','Hello')
    print(res.group())
    # He
    #
    # 总结1：匹配两个字母
    # re.match 是从字符串的开头开始匹配

    res = re.match('\d\d','234')
    print(res.group())
    # 23
    # 总结2：匹配两个数字，也可以写成 re.match('\d{2}','234')

    res = re.match('\s\s\s.','   %hh')
    print(res.group())

    # 总结3：\s表示空格或tab，
    # 总结4：点 表示字母、数字、标点符号、空格、中文等任意内容

    # 练习题
    # -----------------------------------------1: 匹配电子邮件地址--------------------------------------------
    # 编写一个正则表达式来匹配电子邮件地址。
    # ‌示例电子邮件地址：‌
    # example @ example.com
    # 总结5：\w：数字、字母、汉字、下划线；与点的不同是，点比\w多了标点符号
    res = re.match('\w*\s*@\s*\w*.com','example @ example.com')
    print(res.group())
    # 总结6：*表示0到多个，+表示1到多个，？表示0或1个

    # res = re.match('(\w*)\s@\s\1.com','example @ example.com')
    # 总结7：分组匹配：(?P<分组名>正则表达式)   (?P=分组名)  为了后面不重复写跟前面匹配到的内容一样的内容，而非替换一模一样的正则表达式
    res = re.match('(?P<L1>\w*)(?P<L2>\s)@(?P=L2)(?P=L1).com', 'example @ example.com')
    print(res.group())


    # user @ sub.example.com
    res = re.match('\w*\s@\s\w*.\w*.\w*','user @ sub.example.com')
    print(res.group())
    # res = re.match('(?P<L1>\w*)\s@\s(?P=L1).(?P=L1).(?P=L1)','user @ sub.example.com')
    # 上面这样用分组匹配就无法匹配到，因为字符串里没有前后一样的文字内容

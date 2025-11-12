import re

if __name__ == '__main__':
    res = re.match('[a-zA-Z][a-zA-Z]','Hello')
    print(res.group())
    # He

    res = re.match('\d\d','234')
    print(res.group())
    # 23

    res = re.match('\s\s\s.','   hhh')
    print(res.group())
    #    h

    # 练习题
    # -----------------------------------------1: 匹配电子邮件地址--------------------------------------------
    # 编写一个正则表达式来匹配电子邮件地址。
    # ‌示例电子邮件地址：‌
    # example @ example.com
        # \w：数字、字母、汉字、下划线；\s : 空格或tab
    res = re.match('\w*\s*@\s*\w*.com','example @ example.com')
    print(res.group())

    # res = re.match('(\w*)\s@\s\1.com','example @ example.com')
        # 分组匹配：(?P<分组名>正则表达式)   (?P=分组名)  为了后面不重复写跟前面匹配到的内容一样的内容，而非替换一模一样的正则表达式
    res = re.match('(?P<L1>\w*)(?P<L2>\s)@(?P=L2)(?P=L1).com', 'example @ example.com')
    print(res.group())


    # user @ sub.example.com
    res = re.match('\w*\s@\s\w*.\w*.\w*','user @ sub.example.com')
    print(res.group())
    # res = re.match('(?P<L1>\w*)\s@\s(?P=L1).(?P=L1).(?P=L1)','user @ sub.example.com')
    # 上面这样用分组匹配就无法匹配到，因为字符串里没有前后一样的文字内容


    # 练习题 2----------------------------------------- 提取电话号码-----------------------------------------1
    # 编写一个正则表达式来从文本中提取电话号码。电话号码可以是多种格式，例如：
    # (123) 456-7890
    # 123-456-7890
    # 123.456.7890
    # 1234567890
    res = re.search('(\(|\d*)\d*(\)|-|.)?\s?(\d*)?(-|.)?\d*','1234567890')
    print(res.group())

    # 练习题 3-----------------------------------------  查找网址-----------------------------------------
    # 编写一个正则表达式来查找网址（URL）。网址可以是以http: // 或https: // 开头的。
    # ‌示例网址：‌
    # http: // www.example.com
    # https: // www.example.com
    # http: // example.com
    # https: // example.com

    res = re.search('(http: // |https: // )\w*.\w*.\w*','网址是：http: // www.example.com')
    print(res.group())
    res = re.findall('((http: // \w+.\w+.\w+)|(https: // \w+.\w+.\w+))', '网址是：http: // www.example.com;https: // www.example.com')
    print(res)

    text = "John Doe is 30 years old, and Jane Smith is 25."
    people = re.findall(r'(\w+)\s+(\w+)\s+is\s+(\d+)\s+years\s+old', text)
    pe1 =  re.search(r'(\w+)\s+(\w+)\s+is\s+(\d+)\s+years\s+old', text,2)
    print(people)
    print(pe1.group())
    for name, surname, age in people:
        print(f"{name} {surname} is {age} years old.")
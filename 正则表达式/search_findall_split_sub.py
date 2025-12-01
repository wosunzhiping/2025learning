import re

if __name__ == '__main__':

    # 练习题 2----------------------------------------- 提取电话号码-----------------------------------------1
    # 编写一个正则表达式来从文本中提取电话号码。电话号码可以是多种格式，例如：
    # (123) 456-7890
    # 123-456-7890
    # 123.456.7890
    # 1234567890

    # 总结1：search():从头到位匹配，返回第一个成功匹配的数据（只匹配一次），用group方法提取

    res = re.search('(\(|\d*)\d*(\)|-|.)?\s?(\d*)?(-|.)?\d*','1234567890')
    print(res.group())

    # 练习题 3-----------------------------------------  查找网址-----------------------------------------
    # 编写一个正则表达式来查找网址（URL）。网址可以是以http: // 或https: // 开头的。
    # ‌示例网址：‌
    # http: // www.example.com
    # https: // www.example.com
    # http: // example.com
    # https: // example.com

    # 总结2：findall():从头到位匹配，返回所有满足条件的数据，以列表形式返回，没有group方法

    res = re.search('(http: // |https: // )\w*.\w*.\w*','网址是：http: // www.example.com。https: // www.example.com。')
    print(res.group())
    res = re.findall('(http: // \w+.\w+.\w+)|(https: // \w+.\w+.\w+)', '网址是：http: // www.example.com ; https: // www.example.com ; http: // www.example1.com ; https: // www.example1.com')
    print(res)

    text = "John Doe is 30 years old, and Jane Smith is 25 years old."
    people = re.findall(r'(\w+)\s+(\w+)\s+is\s+(\d+)\s+years\s+old', text)
    pe1 =  re.search(r'(\w+)\s+(\w+)\s+is\s+(\d+)\s+years\s+old', text,2)
    print(people)
    print(pe1.group())
    for name, surname, age in people:
        print(f"{name} {surname} is {age} years old.")

    # 总结3：sub():替换,被替换的内容、替换后的内容、目标字符串、被替换的次数
    res = re.sub('\w','替换后','hello',1)
    print(res)

    # 总结4：split():以什么作为分割符、目标字符串、最大分割次数
    res = re.split('\d','小2黑3花',1)
    print(res)
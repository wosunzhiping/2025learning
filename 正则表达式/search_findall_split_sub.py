import re

if __name__ == '__main__':

    # 练习题 2----------------------------------------- 提取电话号码-----------------------------------------1
    # 编写一个正则表达式来从文本中提取电话号码。电话号码可以是多种格式，例如：
    # (123) 456-7890
    # 123-456-7890
    # 123.456.7890
    # 1234567890

    # 总结1：search():从头到位匹配，返回第一个成功匹配的数据（只匹配一次），用group方法提取
    # 总结2：正则表达式的字符串表示中，可以用  (表达式)|(表达式)  的方式表示或的关系，\(  \) 匹配半边括号，要加转义字符

    res = re.search('(\(|\d*)\d*(\)|-|.)?\s?(\d*)?(-|.)?\d*','123.456.7890')
    print(res.group())

    # 练习题 3-----------------------------------------  查找网址-----------------------------------------
    # 编写一个正则表达式来查找网址（URL）。网址可以是以http: // 或https: // 开头的。
    # ‌示例网址：‌
    # http: // www.example.com
    # https: // www.example.com
    # http: // example.com
    # https: // example.com

    # 总结3：findall():从头到位匹配，返回所有满足条件的数据，以列表形式返回，没有group方法

    res = re.search('(http: // |https: // )\w*.\w*.\w*','网址是：https: // www.examplee.com。https: // www.example.com。')
    print(res.group())
    res = re.findall('http: // \w+.\w+.\w+', '网址是：http: // www.examplea.com ; http: // www.exampleb.com ; http: // www.examplec.com ; https: // www.exampled.com')
    print(res)

    res = re.findall('(\d+)|(\D+)|(\w+)','1人，2人，3人，4人，5人')
    print(res)
    # 总结4(同总结5)：findall()中正则表达式中如果用了 ｜ 或表示n个表达式或的关系，那么输出的列表中，每个元素都是一个包含n个元素的元组。


    text = "John Doe is 30 years old, and Jane Smith is 25 years old."
    people = re.findall(r'(\w+)\s+(\w+)\s+is\s+(\d+)\s+years\s+old', text)

    text1 = '人 23 young,人 32 old'
    res1 = re.findall(r'人\s+(\d+)\s+(\w+)',text1)
    res2 = re.findall(r'人\s+\d+\s+\w+', text1)
    print(f'加括号的测试结果res1是：{res1}')
    print(f'不加括号的测试结果res2是：{res2}')
    # 总结5：findall()正则表达式中
    #   如果有括号：每个()中的内容，构成输出列表中一个元素(元组)中的一个元素，
    #   如果没有括号：则匹配整个表达式的内容，作为列表的一个元素。


    pe1 =  re.search(r'(\w+)\s+(\w+)\s+is\s+(\d+)\s+years\s+old', text)
    print(f'people是：{people}')
    print(f'pe1.group()是：{pe1.group()}')
    for name, surname, age in people:
        print(f"循环体执行结果是：{name} {surname} is {age} years old.")
    # 总结6：列表中元素为元组，元组中有多个元素，用于for循环取数时，可参考上面例子



    # 总结7：sub():替换,被替换的内容、替换后的内容、目标字符串、被替换的次数
    res = re.sub('\w','替换后','hello',1)
    print(f'替换测试输出：{res}')

    # 总结8：split():以什么作为分割符、目标字符串、最大分割次数
    res = re.split('\d','小2黑3花',1)
    print(res)
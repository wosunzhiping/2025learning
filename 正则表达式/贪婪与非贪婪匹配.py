import re

if __name__ == '__main__':

    # *?，+? 表示非贪婪匹配，即匹配尽可能少的满足条件的内容
    # 没有?,仅有 * 或 + 表示贪婪匹配，即匹配尽可能多满足条件的内容

    res = re.match('em+?','emmmm') # 匹配1个m
    print(res.group())

    res = re.match('em*?','emmmm') # 匹配0个m
    print(res.group())

    res = re.match('em{1,5}','emmmm') #匹配1到5个中最多个
    print(res.group())

    res = re.match('em{1,5}?','emmmm') #匹配1到5个中最少个
    print(res.group())
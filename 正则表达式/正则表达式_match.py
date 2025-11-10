import re

if __name__ == '__main__':
    res = re.match('[a-zA-Z][a-zA-Z]','Hello')
    print(res.group())

    res = re.match('\d\d','234')
    print(res.group())

    res = re.match('\s\s\s.','   hhh')
    print(res.group())


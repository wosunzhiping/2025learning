import re

if __name__ == '__main__':
    # 1. 若要匹配字符串中的 \，要写4个\ ，或者 r + 2个\
    # 2. r'字符串'  这种写法就是将字符串中的转义字符失去转译效果，使其恢复斜杠的含义

    res = re.match('\\\\',r'\name')
    print(res.group())

    res = re.match(r'\\',r'\table')
    print(res.group())
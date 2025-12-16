# 用户输入年份，判断是否为闰年

if __name__ == '__main__':
    year = int(input('请输入年份：'))
    if year % 4 == 0:
        print(f'{year}是闰年')
    else:
        print(f'{year}是平年')

# --- 总结 ----
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    # 逻辑运算符的使用
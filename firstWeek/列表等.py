
if __name__ == '__main__':

#列表解析
    # range(n) = 包前不包后
    # range(i,j) =  i,i+1,i+2...j-1

    # 列表解析1

    s1 = [x**2 for x in range(4)]
    print(s1)

    # 列
    s2 =  [x**2 for x in range(2,8,2) if x%2==0]
    print(s2)


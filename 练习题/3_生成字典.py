# 使用给定的整数n。生成一个字典，该字典包含从1到n(两者都包含)之间的所有整数，然后打印字典。
# 举例：输入8，则输出{1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64}


def create_dict(x):
    my_dict = {}
    for i in range(1,x+1):
        # my_dict[str(i)] = str(i*i)    这样也可以，下面那行的写法也可以，所以，字典里的key和value不一定都得是字符串
        my_dict[i] = i * i
    return my_dict

if __name__ == '__main__':
    print('请输入一个正整数：')
    x = int(input())
    print(create_dict(x))


#-----------总结——————————————
# 添加字典元素，直接用 d[key]=value 来新建字典元素
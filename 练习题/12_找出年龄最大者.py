# 给定一个字典，姓名作为key,年龄最为值，找出年龄最大者，打印其姓名及年龄

if __name__ == '__main__':
    dic = {'张三':18,'李四':50,'王五':29,'赵六':22}
    max_age = 0
    max_name = ''
    for name,age in dic.items():
        if age > max_age:
            max_age = age
            max_name = name
        else:
            continue
    print(f'年龄最大者是：{max_name}，年龄是{max_age}')



    for name,age in dic.items():
        print(name)
        print(age)
        print(name,age)

    for name in dic.keys():
        print(name)

    for age in dic.values():
        print(age)

    for i in dic:
        print(i)


# -- 总结 --
# 1、遍历字典的三种方式：
# 1）遍历键值对：用dic.items(),可以直接取对应的键或者值
#     for name,age in dic.items():
#         print(name)
#         print(age)
#         print(name,age)
# 2）遍历键：用dic.keys()
#     for name in dic.keys():
#         print(name)
# 3）遍历值：用dic.values()
#     for age in dic.values():
#         print(age)
# 2、求最大值： 先预定义一个最大值变量并初始化，然后再循环中比较更新
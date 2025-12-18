# 定义一个函数，接收一个字典作为参数，并返回该字典中所有值的总和

# ------ 我的答案 --------
def sum_dic(dic1):
    print(type(dic1.values()))
    return sum(dic1.values())

dic_init = {'张三':18,'李四':20}
print(sum_dic(dic_init))



# --------参考答案 ----------
def sum_of_dict(dict1):
    sum = 0
    for i in dict1.values():
        sum += i
    return sum
dic_init = {'张三':18,'李四':20}
print(sum_of_dict(dic_init))

#--------总结---------
# 1、获取字典中所有的值：
#    dict1.values()
#    类型：dict_values 一种特殊类型
#    方法：sum(dict1.values()) 可以直接求所有值的和
#    取值：for i in dict1.values() 可以循环取出每一个值
#    注意：不能用索引取dict_values类型中的某一个值

# 定义一个函数，用于交换指定字典的key 和 value





def swap_dict_key_value(dic):
    result = {}
    for i in dic.items():
        print(type(i))
        result[i[1]] = i[0]
    return result



dic1 = {'a':1,'b':2}
print(swap_dict_key_value(dic1))


# ----- 总结 --------
# 1、字典的常用操作：
# 1）for i in dct.keys()
# 2）for i in dct(values)
# 3）for i in dct(items) , 如此读出的i是元组tuple，可以用索引获取元素
#
# 2、创建字典中的键值对：
#   dct[键]=值
#
# 3、读取字典中某键对应的值：dct[键]
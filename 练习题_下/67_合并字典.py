# 定义一个函数，将两个给定字典合并

def combine_dict(dic1,dic2):
    dic_mid = dic1.copy()
    dic_mid.update(dic2)
    return dic_mid



dict1 = {'我':18,'它':20}
dict2 = {'我':19,'物':20}

print(combine_dict(dict1,dict2))


# -------- 总结 ---------
# 1、两个字典合并：
# 1）先拷贝出来一个新字典：dic1.copy()
# 2）再把第二个字典合并过去：dic_mid.update(dic2)
# 3）如果有相同key：则会用第二个字典里的value覆盖第一个
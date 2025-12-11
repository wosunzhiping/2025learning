# 给定一个学生信息列表，根据学生成绩进行排序
# 学生成绩数据格式：复杂列表，元素是字典或元组
# 示例：
# [
#   {'sno':101,'sname':"小张",'sgrade':88},
#   {'sno':102,'sname':"小王",'sgrade':77},
#   {'sno':103,'sname':"小李",'sgrade':99},
#   {'sno':104,'sname':"小赵",'sgrade':66}
# ]


if __name__ == '__main__':
   list =[
     {'sno':101,'sname':"小张",'sgrade':88},
     {'sno':102,'sname':"小王",'sgrade':77},
     {'sno':103,'sname':"小李",'sgrade':99},
     {'sno':104,'sname':"小赵",'sgrade':66}
   ]

   list1 = sorted(list,key=lambda x:x['sgrade'])
   print(list1)



# --- 总结 ----
# 1、匿名函数：lambda
#   1) 当函数逻辑简单，仅使用一次，可以用匿名函数
#   2）格式：lambda 形参1,形参2 : 作为函数返回值的表达式
# 2、sorted()函数：
#    其中的key= 后面，就是列表中每一个元素都要执行的函数，所以不需要在函数中明确函数入参是这个列表，在lambda函数中，形参直接用x即可
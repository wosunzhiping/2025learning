
print('__init__的程序')
#__init__中暴露在外面的内容，在包被import的时候就会自动执行

__all__ = ['pytest1','pytest2']

# __init__中的__all__列表中的模块，是在from 包名 import * 的时候导入的模块，但仅导入这些模块中非__name__='__main__'中的内容

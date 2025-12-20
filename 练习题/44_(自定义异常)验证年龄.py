# 定义一个函数，用于接收年龄，如果不在有效范围内(<0 或 >120)则抛出异常

def is_right_age(age):
    if age not in range(0,121):
        raise Exception('输入年龄不合法')
    return age

if __name__ == '__main__':
    age = int(input('请输入年龄：'))
    try:
        is_right_age(age)
    except Exception as e:
        print(e)
    print('123') # --- 如果不捕获异常并处理，则这里不会运行



#-------总结-------
# 1、在函数中自定义异常：
#   raise Exception('异常的文字描述')
#
# 2、运行中捕获异常：
# 1）如果不捕获异常，那么出现异常后，其后的代码不会被运行；
# 2）捕获异常 except Exception as e: 是把异常信息保存在变量e中，然后可以打印e，该异常信息
# 3）异常被捕获后，程序不会终止，可以继续向后运行
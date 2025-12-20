# 定义一个函数，用于将客户输入的字符串转换为整数，转换成功则输出，转换失败则返回错误信息


# --------- 我的答案 --------------
def back_int(s):
    try:
        return int(s)
    except Exception:
        # print('输入的字符串无法转换为整数')
        return '输入的字符串无法转换为整数'

# s1 = input('请输入一个字符串：')
# print(f'输入的字符串转换为整数后是：{back_int(s1)}')


# --------- 参考答案 --------------
def string_to_int(s):
    try:
        num = int(s)
        print(num)
    except:
        print('输入错误')
    else:
        return num
        # print(num)
    finally:
        return 'finally'
s1 = input('请输入一个字符串：')
print(string_to_int(s1))



# -------总结---------
# 1、捕获异常：
# try: 要执行的代码；
# except: 出现异常要做的处理；
#   except Exception: 这样写也可以，没有指定某具体异常，表示所有异常
# else：不出现异常要做的处理；
# finally：无论是否异常都要执行的动作
#
# 注意：
# 如果try: except: else: finally: 中全部有return，
# 那么最终体现出来的函数返回只有finally中的return。
#
# 但如果他们中都是print，就可以明显看出来，
# 执行了try+else+finally，或者try+except+finally
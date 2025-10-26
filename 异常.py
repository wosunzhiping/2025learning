from package import *

if __name__ == '__main__':

    pytest1.test_out1()
    pytest2.test_out1()




    def login():
        pwd = input('请输入密码：')
        if len(pwd) >= 6:
            print('密码输入成功')
        raise Exception('密码不足6位，输入失败')

    try:
        login()
    except Exception as e:
        print(e)
    print('异常后面的代码还可以继续执行')
    print('\n')

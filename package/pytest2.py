print('这是pytest2主函数之外的函数')
def test_out1():
    print('这是pytest2主函数之外的函数1')
def test_out2():
    print('这是pytest2主函数之外的函数2')


if __name__ == '__main__':
    def test_in1():
        print('这是pytest2 main函数内的函数1')
    def test_in2():
        print('这是pytest2 main函数内的函数2')
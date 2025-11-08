from greenlet import greenlet


def sing():
    print(f'在唱歌')
    g2.switch('huahua')
    print(f'唱完歌了')


def dance(name):
    print(f'{name}在跳舞')
    g1.switch()
    print(f'{name}跳完舞了')




if __name__ == '__main__':
    g1 = greenlet(sing)    # 如果 g1 = greenlet(sing())  中带了()，就创建协程的时候直接执行了，不会需要调用switch才执行
    g2 = greenlet(dance)

    g1.switch()
    g2.switch('花2')      # 如果执行到这里的时候，之前的g2还没执行完，则继续执行完之前的，这里的入参不采用

    # 执行完了就不再执行了，每个greenlet只执行一次
    g1.switch()
    g2.switch('花3')
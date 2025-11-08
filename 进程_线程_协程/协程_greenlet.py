from greenlet import greenlet


def sing():
    print(f'在唱歌')
    print(f'唱完歌了')


def dance(name):
    print(f'{name}在跳舞')
    print(f'{name}跳完舞了')



if __name__ == '__main__':
    g1 = greenlet(sing)
    g2 = greenlet(dance)

    g1.switch()
    g2.switch('花2')
    g1.switch()          #执行完了就不再执行了，每个greenlet只执行一次,xiam
    g2.switch('花3')
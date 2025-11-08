import gevent
import time
# 在mac上安装第三方包；command+shift+h 找到当前编译环境目录名
# python3 -m venv playwright_env/
# source playwright_env/bin/activate
# python3 -m pip install gevent


def sing(name):
    print(f'{name}在唱歌3')
    gevent.sleep(3)
    print(f'{name}唱完歌了')

def dance(name):
    print(f'{name}在跳舞1')
    gevent.sleep(1)
    print(f'{name}跳完舞了')


if __name__ == '__main__':

    g_dance = gevent.spawn(dance, 'huahua')
    g_sing = gevent.spawn(sing, '乐乐')



    g_dance.join()
    g_sing.join()

    # 两个任务里都是gevent.sleep()：
    # 即使只放了一个joint(),两个任务都会同时开始执行，并在sleep的地方自动切换
    # 放了join()的那个会执行完，执行完了就不切回到另一个慢的了。
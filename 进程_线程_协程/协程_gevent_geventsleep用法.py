import gevent
import time
# 在mac上安装第三方包；command+shift+h 找到当前编译环境目录名
# python3 -m venv playwright_env/
# source playwright_env/bin/activate
# python3 -m pip install gevent


def sing(name):
    print(f'{name}在唱歌1')
    gevent.sleep(1)
    print(f'{name}唱完歌了')

def dance(name):
    print(f'{name}在跳舞2')
    gevent.sleep(2)
    print(f'{name}跳完舞了')




if __name__ == '__main__':

    g_dance = gevent.spawn(dance, 'huahua')
    g_sing = gevent.spawn(sing, '乐乐')



    g_dance.join()
    # g_sing.join()


    # 当两个任务里都是gevent.sleep()：
    # 如果只有一个任务写了join()：
    #   两个任务都会同时开始执行，并在sleep的地方自动切换
    #   放了join()的那个会执行完，执行完了就不切回到另一个慢的了。
    # 如果一个join()都不写，则任何一个任务都不会执行
    # 如果两个都写了join(),则不管快慢，两个任务都会切换着执行完

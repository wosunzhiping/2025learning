import gevent
import time

def time_sing(name):
    print(f'{name}用time间隔开始唱歌1')
    time.sleep(1)
    print(f'{name}用time间隔唱完歌了1')

def time_dance(name):
    print(f'{name}用time间隔开始跳舞2')
    time.sleep(2)
    print(f'{name}用time间隔跳完舞了2')


def run(name):
    print(f'{name}用gevent间隔开始跑步3')
    gevent.sleep(3)
    print(f'{name}用gevent间隔跑完步了3')

def read(name):
    print(f'{name}用gevent间隔在看书4')
    gevent.sleep(4)
    print(f'{name}用gevent间隔看完书了4')

if __name__ == '__main__':
    g3 = gevent.spawn(run,'皮皮')
    g1 = gevent.spawn(time_dance,'花花')
    g2 = gevent.spawn(time_sing,'乐乐')
    g4 = gevent.spawn(read,'美美')

    g4.join()
    # 两个任务中都是time.sleep()实现等待
    # 1、如果不写join(),则任何任务都不会执行
    # 2、如果只写一个gevent对象的join():
        # 所有gevent对象都会运行
        # 运行顺序是创建协程的顺序
        # 顺序执行，不会切换，因为只有使用了gevent.sleep()的才会实现自动切换IO

    # 多个任务，混杂着使用了time.sleep() 和 gevent.sleep()的：
    # 1、只有写了join()，才会开始运行任务
    # 2、只写一个join()，会运行所有任务，执行顺序按照协程定义的顺序
        # 1）其中，用time.sleep()的，会顺序、串形运行完
        # 2）用gevent.sleep()的：
            # 只有使用了join()的，才会自动切换到自己运行完，
              # 如果刚好是运行时间长的，那么会自动完成跟另外的含gevent.sleep()时间短的任务的自动切换执行
              # 如果是运行时间短的，那么只会切换回来保证自己运行完，执行完不再切回去其他任务了。
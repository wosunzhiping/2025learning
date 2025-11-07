from multiprocessing import Process
import os


def run(name):
    print(f'{name}在跑步')
    print('当前run进程id是',os.getpid())
    print('当前run进程父进程id是', os.getppid())



def sleep(name):
    print(f'{name}在睡觉')
    print(f'当前sleep进程id是：',os.getpid())
    print('当前sleep进程父进程id是：', os.getppid())


if __name__ == '__main__':
    p1 = Process(target=run,args=('乐乐',),name='跑步进程')       #创建时就定义进程名
    p2 = Process(target=sleep,args=('花花',),name='睡觉进程')     #参数以元组的形式传入，只有一个参数的时候，注意要有逗号

    p1.name = '重命名跑步进程'  #

    p1.start()
    p1.join()    #这里放置阻塞，主程序会等p1子进程执行完再继续后面，所以此时打印p1状态时未存活，p2没有用join，主进程和P2进程同时运行，打印P2状态就是存活
    p2.start()


    print('子进程名字分别是：%s,%s'%(p1.name,p2.name))
    print(f'p1进程id是：{p1.pid}')

    print(f'p1子进程存活状态：{p1.is_alive()}')
    print(f'p2子进程存活状态：{p2.is_alive()}')


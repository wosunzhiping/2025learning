import threading
import time


def run(name):
    print(f'{name}正在跑步')
    time.sleep(2)
    print(f'{name}跑完步了')

def listen(name):
    print(f'{name}正在听歌')
    time.sleep(2)
    print(f'{name}听完歌了')

if __name__  == '__main__':
    # run('乐乐')
    # listen('乐乐')

    # t1 = threading.Thread(target=run('乐乐'))  #错误写法
    # t2 = threading.Thread(target=listen('乐乐')) #错误写法

    # t1 = threading.Thread(target=run,args=('乐乐')) #错误写法：当以元组方式传参，参数只有一个的时候，这个参数后面要有逗号


    t1 = threading.Thread(target=run, args=('乐乐',))
    t2 = threading.Thread(target=listen,args=('乐乐',))
    t1.start()
    t2.start()
    t1.join()  #阻塞主线程，等待子线程执行完再执行主线程
    print('回家休息')
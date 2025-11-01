import threading
import time
#
# def speak(name):
#     print(f'{name}正在说话')
#     print('当前线程名：',threading.current_thread().name)
#     time.sleep(1)
#     print(f'{name}说完话了')
#
# def run(name):
#     print(f'{name}正在跑步')
#     print('当前线程名：',threading.current_thread().name)
#     time.sleep(2)
#     print(f'{name}跑完步了')
#
# def listen(name):
#     print(f'{name}正在听歌')
#     print('当前线程名：',threading.current_thread().name)
#     time.sleep(4)
#     print(f'{name}听完歌了')
#
# if __name__  == '__main__':
#     # run('乐乐')
#     # listen('乐乐')
#
#     # t1 = threading.Thread(target=run('乐乐'))  #错误写法
#     # t2 = threading.Thread(target=listen('乐乐')) #错误写法
#
#     # t1 = threading.Thread(target=run,args=('乐乐')) #错误写法：当以元组方式传参，参数只有一个的时候，这个参数后面要有逗号
#
#     # 1、创建线程
#     # 设置两个线程，分别执行两个方法/任务
#     t_run = threading.Thread(target=run, args=('乐乐',))
#     t_lis = threading.Thread(target=listen,args=('乐乐',))
#     t_spe = threading.Thread(target=speak,args=('lele',))
#
#     # 2、设置线程名字
#     t_run.setName('跑步线程')
#     t_lis.setName('听歌线程')
#     t_spe.setName('说话线程')
#
#     # 3、阻塞线程
#     # 如果要在跑步线程完成后继续其他线程，则要设置阻塞线程
#     # 设置的方法是在线程start之后，设置join。这样设置后，其后的其他线程，包括主线程，都要等本线程执行完才能继续。
#     t_run.start()
#     t_run.join()  #阻塞主线程，等待子线程执行完再执行主线程
#
#
#     # 4、守护线程
#     # 听歌任务作为非必要任务，设置为守护线程，即在主线程结束的时候就结束该线程，即使其对应的方法还没执行完。
#     # 设置的方法是在线程start之前就先setDeamon(True)
#     t_lis.setDaemon(True)
#     t_lis.start()
#     t_spe.start()  #说完话应该在跑完步之前，但是跑步的线程设置了阻塞，并且是在说话之前，所以会体现为跑步完成后才会开始说话
#
#
#
#     # 5、当前线程
#     # 打印线程名字
#     print('打印线程名：',t_run.getName())
#     print('打印线程名：',t_lis.getName())
#     print('当前线程名:',threading.current_thread().name)
#     print('回家休息')


    # 6、线程同步 ： 如果多个线程存在访问同一个资源的情况，需确保多线程可以安全访问共享资源，避免竞争、数据不一致
        # 方式一： 使用join()，阻塞线程，在上一个线程执行完后执行下一个线程
        # 方式二： 加锁，使用lock

number = 0
lock = threading.Lock()

def count():
    lock.acquire()
    for i in range(500000):
        global number
        number += 1
    print(number)
    lock.release()

def count2():
    lock.acquire()
    for i in range(400000):
        global number
        number -= 1
    print(number)
    lock.release()

if __name__ == '__main__':
    t_count = threading.Thread(target=count)
    t_count2 = threading.Thread(target=count2)

    # 如果不加锁，因为两个线程都访问共享资源--全局变量number，会造成混乱(当迭代次数很大的时候才会明显体现出来)
    t_count.start()
    t_count2.start()





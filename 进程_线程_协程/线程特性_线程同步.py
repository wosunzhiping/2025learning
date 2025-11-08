from threading import Thread
from threading import Lock

    # 6、线程同步 ： 如果多个线程存在访问同一个资源的情况，需确保多线程可以安全访问共享资源，避免竞争、数据不一致
        # 方式一： 使用join()，阻塞线程，在上一个线程执行完后执行下一个线程
        # 方式二： 加锁，使用lock

number = 0
lock = Lock()

def count():
    lock.acquire()
    for i in range(5000000):
        global number
        number += 1
    print(number)
    lock.release()

def count2():
    lock.acquire()
    for i in range(4000000):
        global number
        number -= 1
    print(number)
    lock.release()

if __name__ == '__main__':
    t_count = Thread(target=count)
    t_count2 = Thread(target=count2)

    # 如果不加锁，因为两个线程都访问共享资源--全局变量number，会造成混乱(当迭代次数很大的时候才会明显体现出来)
    t_count.start()
    t_count2.start()
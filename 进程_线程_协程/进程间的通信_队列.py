from multiprocessing import Queue
from multiprocessing import Process
import os

a = 0
b = 1000000

def writeData(q,c):
    global a
    print('写进程运行')
    for j in range(b):
        a += 1
    print(f'写进程中的a值为：{a},a的地址是：{id(a)}')

    for k in range(b):
        c += 1
    print(f'写进程中的c值为：{c},c的地址是：{id(c)}')

    print(f'写进程中的Q的地址是：{id(q)}')

    for i in range(6):
        q.put(i)
        print(f'{i}已写入队列')
    print(f'当前进程id:{os.getpid()}')


def readData(q,c):
    global a
    print(f'读进程运行')
    print(f'读进程中读取a值为{a}，a的地址是{id(a)}')  #虽然都声明了是全局变量a，但是多进程中使用的全局变量是不共享资源的。
    print(f'读进程中读取c值为{c}，c的地址是{id(c)}')  #虽然都传入了同一个变量c，但是仍然不是共享的资源
    print(f'读进程中的Q的地址是：{id(q)}')           #但是队列不一样，传入同一个队列，多进程是共享的
    print(f'队列是否为空: {q.empty()}')
    while not q.empty():               #注意，非  的写法是 not
        print(f'{q.get()}已取出')
    print(f'当前进程id:{os.getpid()}')


if __name__ == '__main__':
    testq = Queue()
    # writeData(testq)
    # readData(testq)

    c = 10


    p1 = Process(target=writeData,args=(testq,c),name='写列表进程')
    p2 = Process(target=readData,args=(testq,c),name='读列表进程')

    p1.start()    #进程的执行也是无序的
    p1.join()
    print('\n')
    p2.start()
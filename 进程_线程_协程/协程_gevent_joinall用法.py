import gevent


def my_task(n):
    print(f"任务 {n} 开始")
    gevent.sleep(2)  # 模拟耗时操作
    print(f"任务 {n} 结束")

if __name__ == "__main__":
    # list = [1,2,3,4]
    # for i in range(4):
    #     list[i] = gevent.spawn(my_task,i)
    #
    # list[0].join()

    tasks = [gevent.spawn(my_task, i) for i in range(4)]  # 创建协程列表
    gevent.joinall(tasks)  # 等待所有协程完成
    print("所有任务完成")


    # joinall()的作用，就是显式的写明了哪些任务要同时执行，并且要全部执行完才能继续，
    # 避免了每一个任务都要写一次join()
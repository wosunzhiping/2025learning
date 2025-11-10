import gevent
import time
from gevent import monkey  # 导入模块


# monkey.patch_all()   # 放在这里也可以

def run():
    print('开始跑步')
    time.sleep(1)
    print('跑步结束')

def listen():
    print('开始听歌')
    time.sleep(2)
    print('听歌结束')

if __name__ == '__main__':
    monkey.patch_all()      # 将所有time.sleep全部替换成 gevent.sleep
    tasks = [gevent.spawn(run),gevent.spawn(listen)]
    gevent.joinall(tasks)
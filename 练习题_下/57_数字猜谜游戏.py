# 编写一个程序，实现数字猜谜游戏并测试反应速度。其中数字是0-99间的随机数。

import time
import random

# --------- 我的答案 -----------------
# answer = random.randint(0,99)
# try:
#     guess = int(input('请猜这个数字是什么：'))
#     start_time = time.perf_counter()
#     while True:
#         if guess < answer:
#             guess = int(input('太小了，再猜一次：'))
#         elif guess > answer:
#             guess = int(input('太大了，再猜一次：'))
#         elif guess == answer:
#             end_time = time.perf_counter()
#             used_time = end_time - start_time
#             print(f'恭喜你猜对啦！这个数字是：{answer},您此次游戏耗时{used_time:.2f}s')
#             break
# except ValueError:
#     print('输入数字不合法，请重新输入!')



# --------- 参考答案 -----------------
answer = random.randint(0,99)
try:
    guess = int(input('请猜这个数字是什么：'))
except ValueError:
    print('输入数字不合法，请重新输入!')
else:
    start_time = time.perf_counter()
    while True:
        if guess < answer:
            guess = int(input('太小了，再猜一次：'))
        elif guess > answer:
            guess = int(input('太大了，再猜一次：'))
        elif guess == answer:
            end_time = time.perf_counter()
            used_time = end_time - start_time
            print(f'恭喜你猜对啦！这个数字是：{answer},您此次游戏耗时{used_time:.2f}s')
            break


# --------- 总结 -----------------
# 1、try..except..else
# 1）try 后写可能出现异常的代码，不需要都包进去
# 2）except后面的异常名称可以在报错信息里拷贝出来
# 3）else:后面写如果没有出现except的异常，才会执行的内容，如果不写except，只是捕获了异常不退出程序，还会继续执行后续代码
# 2、f-string方式格式化字符串：
# f'{used_time:.2f}s' 冒号后面写规则
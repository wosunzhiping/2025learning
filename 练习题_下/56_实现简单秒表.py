# 程序在用户按下回车键后开始计时，在中断程序时停止计时

import time

input('准备开始计时...')
print('计时开始...')
start = time.perf_counter()

try:
    while True:
        end = time.perf_counter()
        time_counter = end - start
        time.sleep(1)
        print(f'\r{time_counter:.0f}s',end='')
except KeyboardInterrupt:
    total = time.perf_counter()-start
    print(f'\n计时结束，总耗时：{total:.0f}s')


# ---------- 总结 -----------
# 1、input('准备开始计时...')
#   本身就会获取用户输入的回车，回车后执行其后的程序
#
# 2、print(f'\r{time_counter:.0f}s',end='')
# 1）\r 表示从本行行首开始打印，效果就是循环打印的时候，下一次打印的内容会覆盖上一次打印的内容
# 2）end=''参数，设置打印后行尾把回车替换成什么
# 3）'{time_counter:.0f}s' f-string 方式格式化字符串，设置打印小数的位数
#
# 3、except KeyboardInterrupt:
#   不需要记住exception的名称，当运行终止时，控制台会显示当前的异常名称，拷贝过来就行来


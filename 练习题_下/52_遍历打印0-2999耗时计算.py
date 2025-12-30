# 遍历打印0-2999之间所有的整数，并输出整个过程的耗时

import time

start_time = time.time()
for i in range(0,3000):
    print(i)
end_time = time.time()
use_time = end_time - start_time
print(f'整个过程耗时{use_time}s')


# ---------- 总结 ----------------
# 1、time.time() 得到的是从1970年0点到当前时间的秒数，两个秒数相减，得到的是两个动作的时间差
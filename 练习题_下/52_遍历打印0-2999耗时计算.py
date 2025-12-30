# 遍历打印0-2999之间所有的整数，并输出整个过程的耗时

import time

start_time = time.time()
for i in range(0,3000):
    print(i)
end_time = time.time()
use_time = end_time - start_time
print(f'整个过程耗时{use_time}s')



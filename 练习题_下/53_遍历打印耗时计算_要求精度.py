# 遍历从0-9999所有整数，计算所需时间，并以保留三位小数(不是三位有效数字)的浮点数形式输出

import time

# ---------- 我的答案 ----------------
start_time = time.time()
for i in range(10000):
    continue
end_time = time.time()

time_spend = round((end_time - start_time),3)

print(time_spend)


# ---------- 参考答案 ----------------
start = time.perf_counter()

for i in range(10000):
    print(i)

end = time.perf_counter()


print(f'{end - start:.3f}')
print('{:.3f}'.format(end-start))


# ---------- 总结 ----------------
# 1、time.perf_counter():
#   返回一个高精度的浮点数秒数，表示从程序启动时开始，经过的时间
#
# 2、保留三位小数：
# 1）用round(n,3) -- 四舍五入保留三位小数
# 2）使用格式化字符串：
#   1》 f-string方法：
#       f'{num:.3f}' 在f''字符串中的数字冒号后面写规则
#   2》 format方法：
#       '{:.3f}'.format(num)



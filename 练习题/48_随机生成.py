# 用random生成各种随机数
import random

print(f'0-1(不含1)之间的随机小数：{random.random()}')
print(f'0-100（包前包后）间的随机整数：{random.randint(1,100)}')
print(f'0-100间的随机浮点数：{random.uniform(1,100)}')
print(f'随机返回列表[1,2,3,4,5,6]中的任意元素：{random.choice([1,2,3,4,5,6])}')
print(f'随机返回列表[1,1,2,1,3,3,4,2,4,5]中的5个唯一元素：{random.sample([1,1,2,1,3,3,4,2,4,5],5)}')
l1 =[1,2,3,4,5,6]
random.shuffle(l1)
print(f'打乱列表l1的顺序，原地修改:{l1}')
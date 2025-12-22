# 用python 的tkinter库，来创建一个图形界面，并在其中绘制一个由圆圈组成的螺旋形图案

from tkinter import *


canvs = Canvas(width=400,height=400)

canvs.pack()

i =1
j = 1

while True:
    i += j
    if 50+i >= 350 - i :
        break
    canvs.create_oval(50+i,50+i,350-i,350-i)
    j += 1

mainloop()



# -------- 总结 --------
# 1、tkinter GUI库，绘制图形界面
#    mainloop() 进入tkinter的主事件循环，窗口一直打开
# 2、库中canvas组件，绘制画布
#   1）pack()方法，布置画布
#   2）creat_oval()方法，绘制椭圆，四个坐标分别是椭圆外切矩形的左上角和右下角坐标
# 3、循环中两个变量参与循环，控制增长速度
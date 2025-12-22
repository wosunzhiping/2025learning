# 使用python的tkinter库来创建一个图形界面，在其中绘制一个由矩形组成的螺旋图形

from tkinter import *

canvas = Canvas(width=300,height=300)

canvas.pack()

# 设置初始值
x0,y0 = 145,145
x1,y1 = 150,150

for i in range(10) :
    canvas.create_rectangle(x0-5*i,y0-5*i,x1+5*i,y1+5*i)

mainloop()


# --------总结--------
# 1、tkinter模块：用于创建图形用户界面
# 2、canvas组件：创建画布，可设置属性宽、高、背景颜色
# 3、布局管理器canvas.pack()：将画布布置到窗口中
# 4、canvas.create_rectangle()：绘制矩形
# 5、mainloop()：进入tkinter的主事件循环，保持窗口打开
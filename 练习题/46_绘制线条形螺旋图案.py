# 使用python的tkinter库，创建一个图形界面，在其中用红色线条绘制图案

from tkinter import *

canvas = Canvas(width=200,height=200)

canvas.pack()

k = 5
j = 5

for i in range(5,51,5):
    canvas.create_line(50+k,45+i,50+k,155-i,fill='red')
    k += 5

for j in range(5,51,5):
    canvas.create_line(50+k,45+i+j,50+k,155-i+j,fill='red')
    k += 5

mainloop()


# ------- 总结 -------
# 1、tkinter 模块，  用于创建图形用户界面
# 2、Canvas 组件，用于绘制图形，可设置width、height、bg(背景颜色)
# 3、布置画布：使用pack布局管理器将画布添加到窗口中
# 4、canvas.create_line(四个坐标，fill=, width=)绘制直线
# 5、mainloop() 进入tkinter的主事件循环
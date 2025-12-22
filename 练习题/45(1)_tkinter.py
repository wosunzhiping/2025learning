from tkinter import *
import tkinter

# 实例化一个对话框
root = Tk()

# 实例化一个画布，并与窗口关联
# cv = Canvas(root,width=300,height=400,bg='blue')
cv = Canvas(root)
# 布置画布
cv.pack()

# 在画布上绘制椭圆
cv.create_oval(50,50,150,150,outline='red',fill='yellow',width=1)

#  进入tkinter 的主事件循环，这样窗口就会处于打开状态，并响应客户操作
root.mainloop()
import os

# file = '/Users/zhipingsun/PycharmProjects/AboutHttp/file.txt'
# file.open()

print('---------文件属性，read()，readline()--------')
f = open('file.txt')
print(f.name)
print(f.mode)
print(f.closed)
print(f.read(2))  #read(n)  n如果不传值，或者传负数，默认全部读取；此时文件指针指向了第三个字符，在后面执行读取的时候，从第3个字符开始

while True:
    l = f.readline()    #一次只读一行，执行完，指针移到下一行
    if not l:
        break
    print(l)

f.close()


print('--------readlines()----------')
f = open('file.txt')
content = f.readlines()  #返回的是一个列表，每一行是一个元素
print(content)
for i in content:
    print(i)
f.close()


print('--------open()的几种模式:r,w,a,+--------')
f = open('file.txt','a+')
f.write('添加内容')
print(f.read())     #此时文件指针在文件末尾，所以执行read()函数，什么都读不到
f.close()


print('------tell(),seek()------')
f = open('file1.txt','w+')
f.write('write mode is create or clear first and move point to the end')
po1 = f.tell()  #查询当前文件指针所在位置
print(po1)
f.seek(5,0)   #移动文件指针，第一个表示移动到第几个字节，第二个表示为以哪个为基准移动。0表示以文件开头为基准，1表示当前位置作为参考，2表示文件末尾为参考
po2 = f.tell()
print(po2)
print(f.read())
f.close()

print('----with open() as--编码格式-----')
with open('file2.txt','w+',encoding='UTF-8') as f:
    f.write('今天放假最后一天')
    f.seek(0,0)
    print(f.read())

with open('file3.txt','w+',encoding='UTF-8') as f2:
    f2.write('10月12放假一天')
    f2.seek(0,0)
    print(f2.read())


print('-------图片的读写---------')
with open('/Users/zhipingsun/Documents/2021/python/数据类型.png','rb') as img1:
    img = img1.read()
with open('数据类型_副本.png','wb') as img2:
    img2.write(img)


print('--------OS模块函数的使用，目录操作(import os)-------')
'''最上面已经impoort os了'''
print('''
1、os.rename()
2、os.remove()
3、os.mkdir()
4、os.rmdir()
5、os.getcwd()
6、os.listdir()
''')
with open('rename.txt','w+',encoding='UTF-8') as g:
    g.write('重命名练习')
os.rename('rename.txt','程序换名字.txt')
os.remove('程序换名字.txt')
os.mkdir('新建文件夹')
os.rmdir('新建文件夹')
print(os.getcwd())
print(os.listdir())
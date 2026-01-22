# 定义一个名为 TextFileHandler 的类，该类支持文本文件的读取和写入功能
import os

class TextFileHandler:
    def __init__(self,filename):
        self.filename = filename

# ----- 我的答案 起 ---------
    def read_file(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                print(file.readlines())
        else:
            print('文件不存在')

    def write_to_file(self,content):
        with open(self.filename,'w') as file:
            file.write(content)
# ----- 我的答案 止 ---------


# ------ 参考答案 起 -----------
    def read_file(self):
        try:
            with open(self.filename,'r',encoding='utf-8') as file:
                content = file.read()
        except:
            return '文件不存在'  # 注意这里用return，如果用print，那么函数的返回默认是'None'，主函数打印的时候会打印None
        else:
            return content

    def write_to_file(self,content):
        with open(self.filename,'a',encoding='utf-8') as file:
            file.write(content + '\n')




test_text = TextFileHandler('测试文件.txt')
# test_text.write_to_file('测试')
print(test_text.read_file())


# ---总结---
# 1、使用with open 打开文件，它会自动关闭文件，但需要注意：
# 1）因为with是等缩进的内容执行完再执行关闭文件的，
# 如果return缩进在with里面，就会出现程序已经执行完了，with才要去关闭文件类，就会出问题，
# 所以return不应该有缩进
#             with open(self.filename,'r',encoding='utf-8') as file:
#                 content = file.read()
#               (这里不应缩进)return content
#
# 2、try..except..else：
# else后的内容，是执行try的内容后没有击中except的内容，才会执行的内容。
#
# 3、文件操作类型，'a'是追加写入


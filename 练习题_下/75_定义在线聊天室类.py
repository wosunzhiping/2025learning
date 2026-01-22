# 定义一个在线聊天室类，允许用户加入聊天室、发送消息、查看聊天记录、离开聊天室


class ChatRoom:
    def __init__(self):
        self.members = []
        self.logfile = 'chatlog.txt'

    def add_member(self,name):
        if name in self.members:
            print(f'{name}已是聊天室成员，无需重复添加！')
        else:
            self.members.append(name)
            with open(self.logfile,'a',encoding='utf-8') as f:
                f.write(f'{name}已添加成功！\n')


    def send_message(self,name,message):
        if name not in self.members:
            print(f'{name}并非聊天室成员，无法发送消息！')
        else:
            with open(self.logfile,'a',encoding='utf-8') as f:
                f.write(f'{name}:{message}\n')


    def view_log(self,name):
        if name not in self.members:
            print(f'{name}并非聊天室成员，无法查看消息！')
        else:
            with open(self.logfile,'r',encoding='utf-8') as f:
                print(f.read())

    def leave_room(self,name):
        if name not in self.members:
            print(f'{name}并非聊天室成员，无法操作离开！')
        else:
            self.members.remove(name)
            with open(self.logfile,'a',encoding='utf-8') as f:
                f.write('{name}已成功离开！\n')



talkroom = ChatRoom()
# talkroom.add_member('孙志平')
talkroom.add_member('孙志平')
talkroom.send_message('孙志平','今天教训很深刻')
talkroom.view_log('孙志平')
talkroom.leave_room('孙志平')

# talkroom.send_message('孙志平','今天教训很深刻')


# --- 总结 ---
# 1、判断用户是否存在于列表：
# if name not in list
# if name in self.members:
#
# 2、所有的方法，都先判断异常情况

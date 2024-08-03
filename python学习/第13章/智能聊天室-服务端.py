import time

import wx
from socket import *
import threading
from concurrent.futures import ThreadPoolExecutor
from 千帆模型 import gpt

class Server(wx.Frame):
    def __init__(self):
        # 实例属性
        self.isOn = False  # 服务器的自动状态
        # 创建Socket对象
        self.server_socket = socket()
        # 绑定ip和端口号
        self.server_socket.bind(('0.0.0.0', 8999))
        # 监听
        self.server_socket.listen(5)
        # 保存所有的客户端
        self.client_thread_dic = {}
        # 创建线程池
        self.pool = ThreadPoolExecutor(max_workers=10)
        # 界面布局
        wx.Frame.__init__(self, None, title='聊天室服务端', size=(450, 670), pos=(100, 100))
        # 创建面板
        self.pl = wx.Panel(self)
        # 创建按钮
        # 启动服务器
        self.start_server_btn = wx.Button(self.pl, label='启动服务器', size=(200, 40), pos=(10, 10))
        # 保存聊天记录
        self.save_text_btn = wx.Button(self.pl, label='保存聊天记录', size=(200, 40), pos=(220, 10))
        # 创建聊天内容文本框
        self.text = wx.TextCtrl(self.pl, size=(410, 500), pos=(10, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)

        # 按钮事件绑定
        self.Bind(wx.EVT_BUTTON, self.start_server, self.start_server_btn)
        self.Bind(wx.EVT_BUTTON, self.save_text, self.save_text_btn)

    def start_server(self, event):
        if not self.isOn:
            print('启动多人聊天室')
            self.isOn = True
            # 创建现场
            main_thread = threading.Thread(target=self.main_thread_fun)
            # 设置为守护线程
            main_thread.daemon = True
            # 启动线程
            main_thread.start()

    # 主线程函数
    def main_thread_fun(self):
        while self.isOn:
            client_socket, client_addr = self.server_socket.accept()
            print('来自客户端连接', client_addr)
            client_name = client_socket.recv(1023).decode('utf8')
            print('客户端名称', client_name)
            client_thread = ClientThread(client_socket, client_name, self)
            # 保存客户端
            self.client_thread_dic[client_name] = client_thread
            self.pool.submit(client_thread.run)
            self.send("【服务器通知】欢迎%s进入聊天室" % client_name)

    def send(self, text):
        self.text.AppendText(text + "\n")
        for client in self.client_thread_dic.values():
            if client.isOn:
                client.client_socket.send(text.encode('utf8'))

    def save_text(self, event):
        print('save_text')
        record = self.text.GetValue()
        with open('record.log', 'a+', encoding='utf-8') as f:
            f.write(record)


class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_name, server):
        super().__init__()
        self.client_socket = client_socket
        self.client_name = client_name
        self.server = server
        self.isOn = True

    def run(self):
        while self.isOn:
            text = self.client_socket.recv(10240).decode('utf8')
            if text == '断开连接':
                self.isOn = False
                self.server.send("【服务器通知】%s离开聊天室" % self.client_name)
            else:
                result = gpt(text)
                print('result', result)
                self.client_socket.send(("【GPT】" + result).encode('utf8'))
                print('发送成功')
                # 等待一段时间，让消息到达接收方
                time.sleep(0.1)
                # self.server.send("【%s】%s" % (self.client_name, text))
        self.client_socket.close()


# 程序的入口
if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()
    # 创建服务器窗口
    server = Server()
    # 显示服务器窗口
    server.Show()
    # 循环显示
    app.MainLoop()

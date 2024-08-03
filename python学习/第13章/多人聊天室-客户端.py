import time

import wx
from socket import *
import threading
from faker import Faker


class Client(wx.Frame):
    # 构造方法
    def __init__(self):
        # 实例属性
        self.name = Faker('zh_CN').name()  # 客户端名字
        self.isConnected = False  # 客户端是否连接服务器
        self.client_sockt = None

        # 界面布局
        wx.Frame.__init__(self, None, title=self.name + '聊天室客户端', size=(450, 670), pos=(600, 100))
        # 创建面板
        self.pl = wx.Panel(self)
        # 创建按钮
        # 加入聊天室
        self.conn_btn = wx.Button(self.pl, label='加入聊天室', size=(200, 40), pos=(10, 10))
        # 离开聊天室
        self.dis_btn = wx.Button(self.pl, label='离开聊天室', size=(200, 40), pos=(220, 10))
        # 清空按钮
        self.clear_btn = wx.Button(self.pl, label='清空', size=(200, 40), pos=(10, 580))
        # 发送按钮
        self.send_btn = wx.Button(self.pl, label='发送', size=(200, 40), pos=(220, 580))
        # 创建聊天内容文本框
        self.text = wx.TextCtrl(self.pl, size=(410, 400), pos=(10, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        # 创建输入内容文本框
        self.input_text = wx.TextCtrl(self.pl, size=(410, 100), pos=(10, 470), style=wx.TE_MULTILINE)

        # 按钮事件绑定
        self.Bind(wx.EVT_BUTTON, self.conn, self.conn_btn)
        self.Bind(wx.EVT_BUTTON, self.dis, self.dis_btn)
        self.Bind(wx.EVT_BUTTON, self.clear, self.clear_btn)
        self.Bind(wx.EVT_BUTTON, self.send, self.send_btn)

    # 点击加入聊天室按钮出发
    def conn(self, event):
        if not self.isConnected:
            print('加入聊天室')
            self.isConnected = True
            self.client_sockt = socket()
            self.client_sockt.connect(('127.0.0.1', 8999))
            # 发送用户名
            self.client_sockt.send(self.name.encode('utf8'))
            # 接收信息主线程
            main_thread = threading.Thread(target=self.recv_data)
            main_thread.daemon = True
            main_thread.start()

    def recv_data(self):
        while self.isConnected:
            text = self.client_sockt.recv(1024).decode('utf8')
            self.text.AppendText(text + '\n')

    # 点击离开聊天室按钮出发
    def dis(self, event):
        print('dis')
        self.client_sockt.send('断开连接'.encode('utf8'))
        time.sleep(1)
        self.isConnected = False
        self.client_sockt.close()

    # 点击清空按钮出发
    def clear(self, event):
        print('clear')
        self.input_text.Clear()

    # 点击发送按钮出发
    def send(self, event):
        print('send')
        if self.isConnected:
            text = self.input_text.GetValue()
            if text:
                self.client_sockt.send(text.encode('utf8'))
                self.input_text.Clear()

# 程序入口
if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()
    # 创建客户端窗口
    client = Client()
    # 显示客户端窗口
    client.Show()
    # 一直循环显示
    app.MainLoop()

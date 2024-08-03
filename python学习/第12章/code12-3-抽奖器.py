import wx
import random


class MyFrame(wx.Frame):
    NameList = ['mia', 'tom', 'jack', 'lili']

    # 构造方法
    def __init__(self):
        wx.Frame.__init__(self, None, title='抽奖器')
        # 创建面板
        self.pl = wx.Panel(self)
        # 设置背景颜色
        self.SetBackgroundColour(wx.GREEN)
        # 创建静态文本
        self.staticText = wx.StaticText(self.pl, label=random.choice(MyFrame.NameList), pos=(100, 50))
        # 创建字体
        font = wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        # 静态文本设置字体
        self.staticText.SetFont(font)

        # 创建按钮
        self.btn1 = wx.Button(self.pl, label='开始抽奖', pos=(100, 100))
        self.btn2 = wx.Button(self.pl, label='结束抽奖', pos=(200, 100))

        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.onClick, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.stop, self.btn2)

        # 创建一个定时器
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_name, self.timer)

    def onClick(self, event):
        # print('click')
        # self.staticText.SetLabelText(random.choice(MyFrame.NameList))
        self.timer.Start(200)  # 每隔200毫秒执行一次

    def update_name(self, event):
        self.staticText.SetLabelText(random.choice(MyFrame.NameList))

    def stop(self, event):
        self.timer.Stop()

if __name__ == '__main__':  # python程序住入口
    # 创建应用程序对象
    app = wx.App()

    # 创建窗口
    frm = MyFrame()
    # 显示窗口
    frm.Show()

    # 让窗口一直显示
    app.MainLoop()

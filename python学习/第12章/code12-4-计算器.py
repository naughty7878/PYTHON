import wx


class MyFrame(wx.Frame):
    pos_x, pos_y = 10, 70
    btn_w, btn_h = 50, 50

    def __init__(self):
        # 创建窗口
        wx.Frame.__init__(self, None, title='简单计算器', pos=(100, 100), size=(265, 410))
        # 创建面板
        self.pl = wx.Panel(self, pos=(0, 0), size=(265, 410))
        # 创建文本框
        self.entry = wx.TextCtrl(self.pl, pos=(10, 10), size=(230, 50), style=wx.TE_RIGHT)
        # 创建按钮
        # 第一行
        self.btn_clear = wx.Button(self.pl, label='C', pos=(MyFrame.pos_x, MyFrame.pos_y),
                                   size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_div = wx.Button(self.pl, label='/', pos=(MyFrame.pos_x + 60, MyFrame.pos_y),
                                 size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_mul = wx.Button(self.pl, label='*', pos=(MyFrame.pos_x + 60 * 2, MyFrame.pos_y),
                                 size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_back = wx.Button(self.pl, label='<-', pos=(MyFrame.pos_x + 60 * 3, MyFrame.pos_y),
                                  size=(MyFrame.btn_w, MyFrame.btn_h))
        # 第二行
        self.btn_7 = wx.Button(self.pl, label='7', pos=(MyFrame.pos_x, MyFrame.pos_y + 60),
                               size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_8 = wx.Button(self.pl, label='8', pos=(MyFrame.pos_x + 60, MyFrame.pos_y + 60),
                               size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_9 = wx.Button(self.pl, label='9', pos=(MyFrame.pos_x + 60 * 2, MyFrame.pos_y + 60),
                               size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_sub = wx.Button(self.pl, label='-', pos=(MyFrame.pos_x + 60 * 3, MyFrame.pos_y + 60),
                                 size=(MyFrame.btn_w, MyFrame.btn_h))
        # 第三行
        self.btn_4 = wx.Button(self.pl, label='4', pos=(MyFrame.pos_x, MyFrame.pos_y + 60 * 2),
                               size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_5 = wx.Button(self.pl, label='5', pos=(MyFrame.pos_x + 60, MyFrame.pos_y + 60 * 2),
                               size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_6 = wx.Button(self.pl, label='6', pos=(MyFrame.pos_x + 60 * 2, MyFrame.pos_y + 60 * 2),
                               size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_add = wx.Button(self.pl, label='+', pos=(MyFrame.pos_x + 60 * 3, MyFrame.pos_y + 60 * 2),
                                 size=(MyFrame.btn_w, MyFrame.btn_h))
        # 第四行
        self.btn_1 = wx.Button(self.pl, label='1', pos=(MyFrame.pos_x, MyFrame.pos_y + 60 * 3),
                               size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_2 = wx.Button(self.pl, label='2', pos=(MyFrame.pos_x + 60, MyFrame.pos_y + 60 * 3),
                               size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_3 = wx.Button(self.pl, label='3', pos=(MyFrame.pos_x + 60 * 2, MyFrame.pos_y + 60 * 3),
                               size=(MyFrame.btn_w, MyFrame.btn_h))
        self.btn_eq = wx.Button(self.pl, label='=', pos=(MyFrame.pos_x + 60 * 3, MyFrame.pos_y + 60 * 3),
                                size=(MyFrame.btn_w, MyFrame.btn_h + 60))
        # 第五行
        self.btn_0 = wx.Button(self.pl, label='0', pos=(MyFrame.pos_x, MyFrame.pos_y + 60 * 4),
                               size=(MyFrame.btn_w + 60, MyFrame.btn_h))
        self.btn_point = wx.Button(self.pl, label='.', pos=(MyFrame.pos_x + 60 * 2, MyFrame.pos_y + 60 * 4),
                                   size=(MyFrame.btn_w, MyFrame.btn_h))

        # 绑定按钮对应的事件
        self.Bind(wx.EVT_BUTTON, self.On_btn_clear, self.btn_clear)
        self.Bind(wx.EVT_BUTTON, self.On_btn_div, self.btn_div)
        self.Bind(wx.EVT_BUTTON, self.On_btn_mul, self.btn_mul)
        self.Bind(wx.EVT_BUTTON, self.On_btn_back, self.btn_back)
        self.Bind(wx.EVT_BUTTON, self.On_btn_sub, self.btn_sub)
        self.Bind(wx.EVT_BUTTON, self.On_btn_add, self.btn_add)
        self.Bind(wx.EVT_BUTTON, self.On_btn_eq, self.btn_eq)
        self.Bind(wx.EVT_BUTTON, self.On_btn_9, self.btn_9)
        self.Bind(wx.EVT_BUTTON, self.On_btn_8, self.btn_8)
        self.Bind(wx.EVT_BUTTON, self.On_btn_7, self.btn_7)
        self.Bind(wx.EVT_BUTTON, self.On_btn_6, self.btn_6)
        self.Bind(wx.EVT_BUTTON, self.On_btn_5, self.btn_5)
        self.Bind(wx.EVT_BUTTON, self.On_btn_4, self.btn_4)
        self.Bind(wx.EVT_BUTTON, self.On_btn_3, self.btn_3)
        self.Bind(wx.EVT_BUTTON, self.On_btn_2, self.btn_2)
        self.Bind(wx.EVT_BUTTON, self.On_btn_1, self.btn_1)
        self.Bind(wx.EVT_BUTTON, self.On_btn_0, self.btn_0)
        self.Bind(wx.EVT_BUTTON, self.On_btn_point, self.btn_point)

    def On_btn_0(self, event):
        self.entry.AppendText('0')

    def On_btn_1(self, event):
        self.entry.AppendText('1')

    def On_btn_2(self, event):
        self.entry.AppendText('2')

    def On_btn_3(self, event):
        self.entry.AppendText('3')

    def On_btn_4(self, event):
        self.entry.AppendText('4')

    def On_btn_5(self, event):
        self.entry.AppendText('5')

    def On_btn_6(self, event):
        self.entry.AppendText('6')

    def On_btn_7(self, event):
        self.entry.AppendText('7')

    def On_btn_8(self, event):
        self.entry.AppendText('8')

    def On_btn_9(self, event):
        self.entry.AppendText('9')

    def On_btn_add(self, event):
        self.entry.AppendText('+')

    def On_btn_sub(self, event):
        self.entry.AppendText('-')

    def On_btn_mul(self, event):
        self.entry.AppendText('*')

    def On_btn_div(self, event):
        self.entry.AppendText('/')

    def On_btn_eq(self, event):
        text = self.entry.GetValue()
        result = eval(text)
        self.entry.SetValue(str(result))
    def On_btn_clear(self, event):
        self.entry.Clear()

    def On_btn_point(self, event):
        self.entry.AppendText('.')

    def On_btn_back(self, event):
        text = self.entry.GetValue()
        self.entry.SetValue(text[:-1])


if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()

    # 创建窗口
    frm = MyFrame()
    # 显示窗口
    frm.Show()

    # 一直显示
    app.MainLoop()

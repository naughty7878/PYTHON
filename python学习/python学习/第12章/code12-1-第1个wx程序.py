import wx

def onClick(event):
    print('按钮被点击了')

# 创建应用程序对象
app = wx.App()
# 创建窗口
# size:宽, 高  pos:x坐标 y坐标
frm = wx.Frame(None, title='python学习系统', size=(400, 600), pos=(200, 100))
# 显示窗口
frm.Show()
# 创建面板
pl = wx.Panel(frm, size=(400, 600))
# 显示面板
pl.Show()
# 创建静态文本
staticText = wx.StaticText(pl, label='欢迎学习python', pos=(100, 50))
# 显示静态文本
staticText.Show()
# 创建按钮
btn = wx.Button(pl, label='测试', pos=(100, 150))
# 显示按钮
btn.Show()
# 按钮绑定事件
frm.Bind(wx.EVT_BUTTON, onClick, btn)

# 进入主循环，让窗口一直限制
app.MainLoop()

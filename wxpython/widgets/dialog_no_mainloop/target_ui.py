import wx

APP_SIZE_X = 300
APP_SIZE_Y = 200

class MyButtons(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(APP_SIZE_X, APP_SIZE_Y))

        wx.Button(self, 1, 'Hello', (50, 130))
        wx.Button(self, 2, 'Close', (150, 130))

        self.Bind(wx.EVT_BUTTON, self.OnHello, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=2)

        self.Centre()
        self.ShowModal()
        self.Destroy()

    def OnClose(self, event):
	print 'close'
        self.Close(True)

    def OnHello(self, event):
	print 'hello'
        self.SetTitle('Hello World!')
	print self.GetTitle()

class MyApp(wx.App):
    def OnInit(self):
        MyButtons(None, -1, 'wxPython GUI')
        return True

if __name__ == '__main__':
    app = MyApp(0)

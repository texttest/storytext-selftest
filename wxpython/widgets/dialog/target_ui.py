
import wx

APP_SIZE_X = 300
APP_SIZE_Y = 200

class MyDialog(wx.Dialog):
    def __init__(self, parent, id):
        wx.Dialog.__init__(self, parent, id, 'wx.Dialog')
        self.button = wx.Button(self, 2, 'Close Dialog', (25, 0))
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)
        #self.Bind (wx.EVT_CLOSE, self.OnClose)

    def OnButton(self, event):
        print 'hihihi'
        self.Close(True)

    '''
    def OnClose(self, event):
        self.EndModal(1)
    '''

class MainFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Test wx.Dialog', size=(APP_SIZE_X, APP_SIZE_Y)) 

        wx.Button(self, 1, 'Show Dialog', (50, 130))
        wx.Button(self, 2, 'Close Frame', (150, 130))

        self.Bind (wx.EVT_BUTTON, self.OnOpen, id=1)
        self.Bind (wx.EVT_BUTTON, self.OnClose, id=2)

    def OnOpen(self, event):
        self.my_dialog = MyDialog(self, -1)
        self.my_dialog.ShowModal()

    def OnClose(self, event):
        self.Close(True)

class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        self.frame = MainFrame(None, -1)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()

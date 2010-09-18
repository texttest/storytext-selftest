
import wx
APP_SIZE_X = 175
APP_SIZE_Y = 75

class MainFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'wx.TextCtrl', size=(APP_SIZE_X, APP_SIZE_Y)) 

        self.tc = wx.TextCtrl(self, 1, 'PyUseCase')
        self.Bind(wx.EVT_TEXT, self.OnText, id=1)

    def OnText(self, event):
        print 'Text:', self.tc.GetValue()

class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        self.frame = MainFrame(None, -1)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()

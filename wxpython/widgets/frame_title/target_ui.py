
import wx
APP_SIZE_X = 150
APP_SIZE_Y = 100


class MainFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'wx.Frame', size=(APP_SIZE_X, APP_SIZE_Y)) 

        self.tc = wx.TextCtrl(self, 1, 'wx.Frame', (25, 0))
        self.button = wx.Button(self, 2, 'Change Title', (25, 25))
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, event):
        new_title = self.tc.GetValue()
        self.SetTitle(new_title)

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

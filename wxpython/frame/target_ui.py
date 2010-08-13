
import wx
APP_SIZE_X = 175
APP_SIZE_Y = 150


class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        self.frame = wx.Frame(None, -1)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()

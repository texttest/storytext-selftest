
import wx

APP_SIZE_X = 300
APP_SIZE_Y = 200

# GUI Frame class that spins off the worker thread
class MainFrame(wx.Frame):
    """Class MainFrame."""
    def __init__(self, parent, id):
        """Create the MainFrame."""
        wx.Frame.__init__(self, parent, id, 'wxPython GUI', size=(APP_SIZE_X, APP_SIZE_Y))

        wx.Button(self, 1, 'Hello', (50, 130))
        wx.Button(self, 2, 'Close', (150, 130))

        self.Bind (wx.EVT_BUTTON, self.OnHello, id=1)
        self.Bind (wx.EVT_BUTTON, self.OnClose, id=2)

    def OnClose(self, event):
        self.Close(True)

    def OnHello(self, event):
        print 'Hello World!'
        
    
class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        """Init Main App."""
        self.frame = MainFrame(None, -1)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()

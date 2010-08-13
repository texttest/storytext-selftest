
import wx

APP_SIZE_X = 175
APP_SIZE_Y = 150

class MainFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'wx.ListCtrl', size=(APP_SIZE_X, APP_SIZE_Y)) 

        self.lc = wx.ListCtrl(self, 1, style=wx.LC_REPORT)
        self.lc.InsertColumn(0, 'numbers')
        for label in ["zero", "one", "two", "three", "four"]:
            item = wx.ListItem()
            item.SetText(label)
            self.lc.InsertItem(item)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSelect, id=1)

    def OnSelect(self, event):
        print 'Selected', self.lc.GetItemText(event.GetIndex())

class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        self.frame = MainFrame(None, -1)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()

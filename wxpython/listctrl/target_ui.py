#!/usr/bin/python

# capitals.py

import wx

APP_SIZE_X = 175
APP_SIZE_Y = 125

class MainFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'wx.ListCtrl', size=(APP_SIZE_X, APP_SIZE_Y)) 

        self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.lc.InsertColumn(0, 'number')
        self.lc.InsertColumn(1, 'english')
        i = 0
        for item in ["one", "two", "three", "four"]:
            self.lc.InsertStringItem(i, str(i))
            self.lc.SetStringItem(i, 1, item)
            i += 1

    def OnClose(self, event):
        self.Close()

class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        self.frame = MainFrame(None, -1)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()

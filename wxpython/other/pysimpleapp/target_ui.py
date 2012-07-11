
import wx

#----------------------------------------------------------------------

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size=(300, 300))
        
        self.panel = wx.Panel(self, -1, size=(300, 300), name='panel')
        self.panel.SetBackgroundColour((150, 150, 150))
        sizer = wx.BoxSizer(wx.VERTICAL)
        button1 = wx.Button(self.panel, -1, 'Button 1', name='Rufus')
        self.Bind(wx.EVT_BUTTON, self.onButton1, button1)
        button2 = wx.Button(self.panel, -1, 'Button 2', name='Sally-Anne')
        self.Bind(wx.EVT_BUTTON, self.onButton2, button2)
        sizer.Add(button1, 0, wx.ALIGN_CENTER)
        sizer.Add(button2, 0, wx.ALIGN_CENTER)
        
        self.panel.SetSizer(sizer)
        
        
    def onButton1(self, event):
        print event.GetEventObject().GetName()
        
        
    def onButton2(self, event):
        print event.GetEventObject().GetName()



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Frame()
    frame.Show(True)
    app.MainLoop()
    


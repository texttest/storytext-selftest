# dbutton.py  --  Create a button dynamically, i.e., in response to user input

import wx

ID_CONTINUE_BUTTON = wx.NewId()

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Dynamic Button", pos=(150,150), size=(350,200))

        self.panel = wx.Panel(self)

        box = wx.BoxSizer(wx.VERTICAL)
        
        m_text = wx.StaticText(self.panel, -1, "Press the OK button")
        m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        m_text.SetSize(m_text.GetBestSize())
        box.Add(m_text, 0, wx.ALL, 10)

        buttonOK = wx.Button(self.panel, wx.ID_OK, "OK")
        buttonOK.Bind(wx.EVT_BUTTON, self.OnOK)
        box.Add(buttonOK, 0, wx.ALL, 10)
        
        self.panel.SetSizer(box)
        self.panel.Layout()

    def OnOK(self, event):
        self.SetTitle("OK clicked: Now click on Continue")
        self.createButton()

    def createButton(self):
        continueButton = wx.Button(self.panel, ID_CONTINUE_BUTTON, "Continue")
        continueButton.SetName("Continue")
        continueButton.Bind(wx.EVT_BUTTON, self.OnContinue)
        self.panel.GetSizer().Add(continueButton, 0, wx.ALL, 10)
        self.panel.Layout()

    def OnContinue(self, event):
        self.SetTitle("Continue Button Was Pressed")
        

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()


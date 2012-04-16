# choice.py -- wx.Choice exercise
#
# Started as:
# Chapter 3: An Applications Building Blocks, Basic Controls
# Recipe 5: Choice Control
#
import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Choice Exercise")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = ChoicePanel(self)

        # Layout
        self.CreateStatusBar()

class ChoicePanel(wx.Panel):
    def __init__(self, parent):
        super(ChoicePanel, self).__init__(parent)

        # Attributes
        items = ["item A", "item B", "item C", "item D"]
        self.choice = wx.Choice(self, choices=items, name="My Choice")
        self.choice.SetSelection(wx.NOT_FOUND)

        # Layout
        sizer = wx.BoxSizer()
        sizer.Add(self.choice, 1, wx.ALIGN_TOP|wx.ALL, 20)
        self.SetSizer(sizer)

        # Event Handlers
        self.Bind(wx.EVT_CHOICE, self.OnChoice)

    def OnChoice(self, event):
        selection = self.choice.GetStringSelection()
        index = self.choice.GetSelection()
        text = "Selected Item: '%s' at index %d" % (selection, index)
        self.GetParent().SetTitle(text)


if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()

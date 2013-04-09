# -*- coding: latin-1 -*-

import os.path
import wx

FRAME_TITLE = "Test"


class GuiCreator():

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, FRAME_TITLE, size=(200, 140))
        self._create_panel()

    def _create_panel(self):
        self.panel = wx.Panel(self, -1)
        button_boxsizer = self._create_button_boxsizer()
        self.panel.SetSizer(button_boxsizer)
        button_boxsizer.Fit(self.panel)

    def _create_button_boxsizer(self):
        self.BUTTON_DEFINTIONS = (
            ("Select Dir", self.OnSelectDir),
            ("Close Me", self.OnButtonClose),
        )
        buttons = []
        for label, handler in self.BUTTON_DEFINTIONS:
            button = self._create_button(label, handler)
            buttons.append(button)
        boxsizer = wx.BoxSizer(wx.VERTICAL)
        self._add_buttons_to_sizer(buttons, boxsizer)
        return boxsizer

    def _create_button(self, label, handler):
        button = wx.Button(self.panel, wx.ID_ANY, label)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    def _add_buttons_to_sizer(self, buttons, sizer):
        for button in buttons:
            sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)


class MyFrame(wx.Frame, GuiCreator):

    def __init__(self):
        GuiCreator.__init__(self)

    def OnButtonClose(self, event):
        self.Close(True)

    def OnSelectDir(self, event):
        rv = wx.DirSelector(message="Select a Directory", defaultPath ="C:\\", style=wx.DD_DEFAULT_STYLE)
        if len(rv) == 0:
            self.SetTitle("No dir selected")
        else:
            self.SetTitle("Dir=%s" % rv)

app = wx.App(False)
frame = MyFrame()
frame.Show(True)
app.MainLoop()


# Exercise in using FileDialog.

import wx, os

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="FileDialog Exercise")
        self.frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.file = None
        style = wx.TE_MULTILINE|wx.TE_RICH2
        self.txtctrl = wx.TextCtrl(self, style=style)

        # Setup
        self._SetupMenus()

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.txtctrl, 1, wx.EXPAND)
        self.SetSizer(sizer)

        # Event Handlers
        self.Bind(wx.EVT_MENU,  self.OnOpen,   id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU,  self.OnSaveAs, id=wx.ID_SAVEAS)
        self.Bind(wx.EVT_MENU,  self.OnExit,   id=wx.ID_EXIT)
        self.Bind(wx.EVT_CLOSE, self.OnExit)

    def _SetupMenus(self):
        """Make the frames menus"""
        menub = wx.MenuBar()
        fmenu = wx.Menu()
        fmenu.Append(wx.ID_OPEN,   "Open\tCtrl+O")
        fmenu.AppendSeparator()
        fmenu.Append(wx.ID_SAVEAS, "Save As\tShift+Ctrl+S")
        fmenu.AppendSeparator()
        fmenu.Append(wx.ID_EXIT,   "Exit\tCtrl+Q")
        menub.Append(fmenu, "File")
        self.SetMenuBar(menub)

    #---- Event Handlers ----#

    def OnOpen(self, event):
        """Handle Open"""
        if event.GetId() == wx.ID_OPEN:
            self.DoOpen()
        else:
            event.Skip()

    def OnSaveAs(self, event):
        """Handle SaveAs"""
        if event.GetId() == wx.ID_SAVEAS:
            self.DoSaveAs()
        else:
            event.Skip()

    def OnExit(self, event):
        """Handle window close event"""
        self.Destroy()

    #---- End Event Handlers ----#

    #---- Implementation ----#

    def DoOpen(self):
        """Show file open dialog"""
        dlg = wx.FileDialog(self,
                            message="Open a File",
                            style=wx.FD_OPEN, 
                            defaultDir=os.getcwd())
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.SetTitle("Open " + path)
        else:
            self.SetTitle("Open Dialog Canceled")
        dlg.Destroy()

    def DoSaveAs(self):
        """Show SaveAs dialog"""
        dlg = wx.FileDialog(self,
                            message="Save As",
                            style=wx.FD_SAVE, 
                            defaultDir=os.getcwd())
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.SetTitle("Save as " + path)
        else:
            self.SetTitle("Save As Dialog Canceled")
        dlg.Destroy()
        
    #---- End Implementation ----#

#---- Main Execution ----#

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()

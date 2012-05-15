import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Popup Menu Example")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)
        self.panel = p = wx.Panel(self)
        menu = wx.Menu()
        exit = menu.Append(-1, "Exit")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
                  
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)

        wx.StaticText(p, -1,"Right-click on the panel to show a popup menu",(25,25))

        p.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)

    def OnShowPopup(self, event):
        # only do this part the first time so the events are only bound once
        #
        # Yet another alternate way to do IDs. Some prefer them up top to
        # avoid clutter, some prefer them close to the object of interest
        # for clarity. 
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()
            self.popupID4 = wx.NewId()
            self.popupID5 = wx.NewId()
            self.popupID6 = wx.NewId()
            self.popupID7 = wx.NewId()
            self.popupID8 = wx.NewId()
            self.popupID9 = wx.NewId()

            self.Bind(wx.EVT_MENU, self.OnPopupOne,   id=self.popupID1)
            self.Bind(wx.EVT_MENU, self.OnPopupTwo,   id=self.popupID2)
            self.Bind(wx.EVT_MENU, self.OnPopupThree, id=self.popupID3)
            self.Bind(wx.EVT_MENU, self.OnPopupFour,  id=self.popupID4)
            self.Bind(wx.EVT_MENU, self.OnPopupFive,  id=self.popupID5)
            self.Bind(wx.EVT_MENU, self.OnPopupSix,   id=self.popupID6)
            self.Bind(wx.EVT_MENU, self.OnPopupSeven, id=self.popupID7)
            self.Bind(wx.EVT_MENU, self.OnPopupEight, id=self.popupID8)
            self.Bind(wx.EVT_MENU, self.OnPopupNine,  id=self.popupID9)

        # make a subsubmenu
        ssm = wx.Menu()
        ssm.Append(self.popupID7, "subsubmenu - Seven")
        ssm.Append(self.popupID8, "subsubmenu - Eight")

        # make a submenu
        sm = wx.Menu()
        sm.Append(self.popupID6, "submenu - Six"  )
        sm.AppendSeparator()
        sm.AppendMenu(-1, 'Subsubmenu', ssm)
        sm.AppendSeparator()
        sm.Append(self.popupID9, "submenu - Nine" )

        # make a menu
        menu = wx.Menu()
        menu.Append(self.popupID1, "One"  )
        menu.Append(self.popupID2, "Two"  )
        menu.Append(self.popupID3, "Three")
        menu.Append(self.popupID4, "Four" )
        menu.Append(self.popupID5, "Five" )
        menu.AppendSeparator()
        menu.AppendMenu(-1, 'Submenu', sm)

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.

        self.panel.PopupMenu(menu)
        menu.Destroy()

    def OnPopupOne(self, event):
        self.SetTitle("Popup one\n")

    def OnPopupTwo(self, event):
        self.SetTitle("Popup two\n")

    def OnPopupThree(self, event):
        self.SetTitle("Popup three\n")
        
    def OnPopupFour(self, event):
        self.SetTitle("Popup four\n")

    def OnPopupFive(self, event):
        self.SetTitle("Popup five\n")

    def OnPopupSix(self, event):
        self.SetTitle("Popup six\n")

    def OnPopupSeven(self, event):
        self.SetTitle("Popup seven\n")

    def OnPopupEight(self, event):
        self.SetTitle("Popup eight\n")

    def OnPopupNine(self, event):
        self.SetTitle("Popup nine\n")


    def OnExit(self, event):
        self.Close()

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()


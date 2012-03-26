# mymenu.py

# A simple menu structure for seeing what menu events are emitted when.

import wx

import wx.lib.inspection

TRACE = False
#TRACE = True

# A handy code snippet for mapping event types to event names, from
# http://wxpython-users.1045709.n5.nabble.com/wxEvent-EventType-td2357268.html

# Unfortunately, event types do not map to unique names.  So, the following
# names are excluded from evt_type_name below to make sure that a given 
# event type maps to exactly one name:

dup = ('EVT_MENU_RANGE', 'EVT_TOOL', 'EVT_TOOL_RANGE', 'EVT_MOUSE_EVENTS', \
'EVT_COMMAND_SCROLL', 'EVT_SCROLL', 'EVT_SCROLL_TOP', 'EVT_SCROLL_BOTTOM', \
'EVT_SCROLL_LINEUP', 'EVT_SPIN_UP', 'EVT_SCROLL_LINEDOWN', 'EVT_SPIN_DOWN',\
'EVT_SCROLL_PAGEUP', 'EVT_SCROLL_PAGEDOWN', 'EVT_SCROLL_THUMBTRACK',       \
'EVT_SPIN', 'EVT_SCROLL_THUMBRELEASE', 'EVT_COMMAND_SCROLL_CHANGED',       \
'EVT_SCROLL_CHANGED', 'EVT_SCROLL_ENDSCROLL', 'EVT_SCROLLWIN_TOP',         \
'EVT_JOYSTICK_EVENTS', 'EVT_UPDATE_UI_RANGE', 'EVT_FIND', 'EVT_FIND_NEXT', \
'EVT_FIND_REPLACE', 'EVT_FIND_REPLACE_ALL', 'EVT_FIND_CLOSE',              \
'EVT_TOOL_RCLICKED_RANGE', 'EVT_MENU_HIGHLIGHT_ALL',                       \
'EVT_DETAILED_HELP_RANGE', 'EVT_SPLITTER_DCLICK', 'EVT_SASH_DRAGGED_RANGE',\
'EVT_TASKBAR_CLICK', 'EVT_HELP_RANGE')


evt_type_name = {}
for evt, name in [(getattr(wx,x), x) for x in dir(wx) if x.startswith('EVT_')]:
    if isinstance(evt, wx.PyEventBinder) and name not in dup:
        evt_type_name[evt.typeId] = name


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MenuFrame(None, title="wxPython Menus", 
                        pos=wx.Point(2500, 200), size=wx.Size(700, 500))
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# Ids to use with menus

ID_MENU_A_ITEM_1          = wx.NewId()
ID_MENU_A_ITEM_2          = wx.NewId()
ID_MENU_B_ITEM_3          = wx.NewId()
ID_MENU_B_ITEM_4          = wx.NewId()
ID_SUBMENU_S_ITEM_5       = wx.NewId()
ID_SUBMENU_S_ITEM_6       = wx.NewId()
ID_MENU_C_ITEM_6_5        = wx.NewId()
ID_MENU_C_RADIO_ITEM_7    = wx.NewId()
ID_MENU_C_RADIO_ITEM_8    = wx.NewId()
ID_MENU_C_RADIO_ITEM_9    = wx.NewId()
ID_MENU_C_SUBMENU_ITEM_10 = wx.NewId()
ID_MENU_C_ITEM_10_5       = wx.NewId()
ID_MENU_C_CHECKED_ITEM_11 = wx.NewId()
ID_MENU_C_CHECKED_ITEM_12 = wx.NewId()
ID_MENU_C_CHECKED_ITEM_13 = wx.NewId()
ID_MENU_C_ITEM_13_5       = wx.NewId()
ID_MENU_D_ITEM_14         = wx.NewId()
ID_MENU_D_ITEM_15         = wx.NewId()
ID_MENU_D_ITEM_16         = wx.NewId()
ID_MENU_D_ITEM_17         = wx.NewId()
ID_MENU_D_ITEM_18         = wx.NewId()
ID_MENU_D_ITEM_19         = wx.NewId()
ID_MENU_D_ITEM_19_3       = wx.NewId()
ID_MENU_D_ITEM_19_6       = wx.NewId()
ID_MENU_E_ITEM_20         = wx.NewId()

id_name = {
ID_MENU_A_ITEM_1          : 'ID_MENU_A_ITEM_1',
ID_MENU_A_ITEM_2          : 'ID_MENU_A_ITEM_2',
ID_MENU_B_ITEM_3          : 'ID_MENU_B_ITEM_3',
ID_MENU_B_ITEM_4          : 'ID_MENU_B_ITEM_4',
ID_SUBMENU_S_ITEM_5       : 'ID_SUBMENU_S_ITEM_5',
ID_SUBMENU_S_ITEM_6       : 'ID_SUBMENU_S_ITEM_6',
ID_MENU_C_ITEM_6_5        : 'ID_MENU_C_ITEM_6_5',
ID_MENU_C_RADIO_ITEM_7    : 'ID_MENU_C_RADIO_ITEM_7',
ID_MENU_C_RADIO_ITEM_8    : 'ID_MENU_C_RADIO_ITEM_8',
ID_MENU_C_RADIO_ITEM_9    : 'ID_MENU_C_RADIO_ITEM_9',
ID_MENU_C_SUBMENU_ITEM_10 : 'ID_MENU_C_SUBMENU_ITEM_10',
ID_MENU_C_ITEM_10_5       : 'ID_MENU_C_ITEM_10_5',
ID_MENU_C_CHECKED_ITEM_11 : 'ID_MENU_C_CHECKED_ITEM_11',
ID_MENU_C_CHECKED_ITEM_12 : 'ID_MENU_C_CHECKED_ITEM_12',
ID_MENU_C_CHECKED_ITEM_13 : 'ID_MENU_C_CHECKED_ITEM_13',
ID_MENU_C_ITEM_13_5       : 'ID_MENU_C_ITEM_13_5',
ID_MENU_D_ITEM_14         : 'ID_MENU_D_ITEM_14',
ID_MENU_D_ITEM_15         : 'ID_MENU_D_ITEM_15',
ID_MENU_D_ITEM_16         : 'ID_MENU_D_ITEM_16',
ID_MENU_D_ITEM_17         : 'ID_MENU_D_ITEM_17',
ID_MENU_D_ITEM_18         : 'ID_MENU_D_ITEM_18',
ID_MENU_D_ITEM_19         : 'ID_MENU_D_ITEM_19',
ID_MENU_D_ITEM_19_3       : 'ID_MENU_D_ITEM_19_3',
ID_MENU_D_ITEM_19_6       : 'ID_MENU_D_ITEM_19_6',
ID_MENU_E_ITEM_20         : 'ID_MENU_E_ITEM_20',
-1 : 'unknown id'
}

class MenuFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MenuFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = wx.Panel(self)
        self.textctrl = wx.TextCtrl(self.panel,
                                   style=wx.TE_MULTILINE)
        self.textctrl.AppendText(
            "Note:  The Change menu changes settings in the Complex menu\n\n")

        # Layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.textctrl, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)
        self.CreateStatusBar() # For output display
#        self.SetStatusText('This text is in the status bar')

        # Setup the Menu
        menuBar = wx.MenuBar()
# This doesn't work; there is no SetParent method
#        menuBar.SetParent(parent=self.panel)
        menuBar.SetName('My MenuBar')

        # Menu A
        menuA = wx.Menu()
        menuA.Append(ID_MENU_A_ITEM_1, "Item 1\tCtrl+A")
        menuA.Append(ID_MENU_A_ITEM_2, "Item 2\tCtrl+B")
        menuBar.Append(menuA, "Menu &A")

        # Menu B
        menuB = wx.Menu()
        menuB.Append(ID_MENU_B_ITEM_3, "Item 3\tCtrl+D")
        menuB.Append(ID_MENU_B_ITEM_4, "Item 4\tCtrl+E")
        menuBar.Append(menuB, "Menu &B")

        # Submenu
        menuS = wx.Menu()
        menuS.SetTitle('Submenu')
        menuS.Append(ID_SUBMENU_S_ITEM_5, "Item 5\tCtrl+F")
        menuS.Append(ID_SUBMENU_S_ITEM_6, "Item 6\tCtrl+G")

        # Complex menu
        menuC = wx.Menu()
        menuC.Append(ID_MENU_C_ITEM_6_5, "Item 6.5")
        self.RadioItem7 = menuC.AppendRadioItem(ID_MENU_C_RADIO_ITEM_7, "Item 7\tCtrl+H")
        self.RadioItem8 = menuC.AppendRadioItem(ID_MENU_C_RADIO_ITEM_8, "Item 8\tCtrl+I")
        self.RadioItem9 = menuC.AppendRadioItem(ID_MENU_C_RADIO_ITEM_9, "Item 9\tCtrl+J")
        menuC.AppendSeparator()
        self.EnableItem10 = menuC.AppendMenu(ID_MENU_C_SUBMENU_ITEM_10, 'Submenu', menuS)
        menuC.AppendSeparator()
        menuC.Append(ID_MENU_C_ITEM_10_5, "Item 10.5")
        self.CheckItem11 = menuC.AppendCheckItem(ID_MENU_C_CHECKED_ITEM_11, "Item 11\tCtrl+K")
        self.CheckItem12 = menuC.AppendCheckItem(ID_MENU_C_CHECKED_ITEM_12, "Item 12\tCtrl+L")
        self.CheckItem13 = menuC.AppendCheckItem(ID_MENU_C_CHECKED_ITEM_13, "Item 13\tCtrl+M")
        menuC.Append(ID_MENU_C_ITEM_13_5, "Item 13.5")
        menuBar.Append(menuC, "&Complex")

        # Change menu menu (Used to change settings on the Complex menu)
        menuD = wx.Menu()
        menuD.Append(ID_MENU_D_ITEM_14, "Check radio item 7")
        menuD.Append(ID_MENU_D_ITEM_15, "Check radio item 8")
        menuD.Append(ID_MENU_D_ITEM_16, "Check radio item 9")
        menuD.AppendSeparator()
        menuD.Append(ID_MENU_D_ITEM_17, "Toggle check item 11")
        menuD.Append(ID_MENU_D_ITEM_18, "Toggle check item 12")
        menuD.Append(ID_MENU_D_ITEM_19, "Toggle check item 13")
        menuD.AppendSeparator()
        menuD.Append(ID_MENU_D_ITEM_19_3, "Toggle enable item 10")
        menuD.Append(ID_MENU_D_ITEM_19_6, "Toggle enable item 11")
        menuBar.Append(menuD, "&Change")

        # A real menu to do real stuff
        menuE = wx.Menu()
        menuE.Append(ID_MENU_E_ITEM_20, "Children of window")
        menuBar.Append(menuE, "&Real Stuff")

        self.SetMenuBar(menuBar)

        # Event Handlers
        self.Bind(wx.EVT_MENU,               self.OnMenu)
        self.Bind(wx.EVT_MENU_OPEN,          self.OnMenuOpen)
        self.Bind(wx.EVT_MENU_CLOSE,         self.OnMenuClose)
        self.Bind(wx.EVT_MENU_HIGHLIGHT,     self.OnMenuHighlight)

    def OnMenu(self, event):
        """Handle clicks on menu items"""
        evt_type = event.GetEventType()
        evt_id   = event.GetId()
        if   evt_id == ID_MENU_D_ITEM_14:
            self.checkMenuItem(self.RadioItem7)
            assert     self.RadioItem7.IsChecked()
            assert not self.RadioItem8.IsChecked()
            assert not self.RadioItem9.IsChecked()
        elif evt_id == ID_MENU_D_ITEM_15:
            self.checkMenuItem(self.RadioItem8)
            assert not self.RadioItem7.IsChecked()
            assert     self.RadioItem8.IsChecked()
            assert not self.RadioItem9.IsChecked()
        elif evt_id == ID_MENU_D_ITEM_16:
            self.checkMenuItem(self.RadioItem9)
            assert not self.RadioItem7.IsChecked()
            assert not self.RadioItem8.IsChecked()
            assert     self.RadioItem9.IsChecked()
        elif evt_id == ID_MENU_D_ITEM_17:
            self.toggleMenuItem(self.CheckItem11)
        elif evt_id == ID_MENU_D_ITEM_18:
            self.toggleMenuItem(self.CheckItem12)
        elif evt_id == ID_MENU_D_ITEM_19:
            self.toggleMenuItem(self.CheckItem13)
        elif evt_id == ID_MENU_D_ITEM_19_3:
            self.toggleEnableMenuItem(self.EnableItem10)
        elif evt_id == ID_MENU_D_ITEM_19_6:
            self.toggleEnableMenuItem(self.CheckItem11)
        elif evt_id == ID_MENU_E_ITEM_20:
            self.findChildrenOfWindow(self)
        tag  = "OnMenu:  type=" + evt_type_name[evt_type]
        tag += " id=" + id_name[evt_id]
#        self.SetStatusText(tag)
        self.SetTitle(tag)
        if TRACE:
            self.textctrl.AppendText(tag+"\n")
        event.Skip()

    def toggleEnableMenuItem(self, menuitem):
        enableStatus = menuitem.IsEnabled()
        menuitem.Enable(not enableStatus)

    def toggleMenuItem(self, menuitem):
        assert menuitem.IsCheckable()
        setting = menuitem.IsChecked()
        menuitem.Check(not setting)

    def checkMenuItem(self, menuitem):
        assert menuitem.IsCheckable()
        menuitem.Check(True)

    def findChildrenOfWindow(self, widget, indent=0):
        if indent == 0:
            self.textctrl.AppendText("\nChildren of this window:  " + 
                                                        str(widget) + "\n")
        indent += 4
        spaces = ' ' * indent
        children = widget.GetChildren()
        for child in children:
            self.textctrl.AppendText(spaces + str(child) + "\n")
            self.findChildrenOfWindow(child, indent=indent)

    def OnMenuOpen(self, event):
        evt_type = event.GetEventType()
        evt_id   = event.GetId()
        tag  = "OnMenuOpen:  type=" + str(evt_type)
        tag += " (" + evt_type_name[evt_type] + ")"
        tag += " id=" + str(evt_id) + " ("
        if evt_id == wx.EVT_MENU_OPEN:
            tag += "EVT_MENU_OPEN"
        else:
            tag += id_name[evt_id]
        tag += ")"
#        self.SetStatusText(tag)
        if TRACE:
            self.textctrl.AppendText("\n"+tag+"\n")
        event.Skip()

    def OnMenuClose(self, event):
        evt_type = event.GetEventType()
        evt_id   = event.GetId()
        tag  = "OnMenuClose:  type=" + str(evt_type)
        tag += " (" + evt_type_name[evt_type] + ")"
        tag += " id=" + str(evt_id) + " ("
        if evt_id == wx.EVT_MENU_CLOSE:
            tag += "EVT_MENU_CLOSE"
        else:
            tag += id_name[evt_id]
        tag += ")"
#        self.SetStatusText(tag)
        if TRACE:
            self.textctrl.AppendText(tag+"\n"+"\n")
        event.Skip()

    def OnMenuHighlight(self, event):
        evt_type = event.GetEventType()
        evt_id   = event.GetId()
        tag  = "OnMenuHighlight:  type=" + str(evt_type)
        tag += " (" + evt_type_name[evt_type] + ")"
        tag += " id=" + str(evt_id) + " ("
        if   evt_id == wx.EVT_MENU_HIGHLIGHT:
            tag += "EVT_MENU_HIGHLIGHT"
        elif evt_id == wx.EVT_MENU_HIGHLIGHT_ALL:
            tag += "EVT_MENU_HIGHLIGHT_ALL"
        elif evt_id == wx.EVT_MENU_RANGE:
            tag += "EVT_MENU_RANGE"
        else:
            tag += id_name[evt_id]
        tag += ")"
#        self.SetStatusText(tag)
# For now, don't display highlight events; there are too many of them and they
# are not of great interest.
#        if TRACE:
#            self.textctrl.AppendText(tag+"\n")
        event.Skip()

class TestMenuBarDescription:

    INDENT = 4  # Indentation increment -- must be positive

    def getMenuBarDescription(self, menubar, indent=INDENT):
        spaces = ' ' * indent
        text = '\nMenubar:\n'
        text += spaces + '>>>\n'
        for menu, label in menubar.GetMenus():
            text += spaces + label + ' (+)\n'
        for menu, label in menubar.GetMenus():
            text += '\n'
            text += self.getMenuDescription(menu, indent)
        return text

    def getMenuDescription(self, menu, indent=0, disabled=''):
        spaces = ' ' * indent
        text = spaces + menu.GetTitle().replace('_', '') + ' menu' + disabled + '\n'
        for item in menu.GetMenuItems():
            text += self.getMenuItemDescription(item, 
                                                indent=indent+self.INDENT)
        return text

    def getMenuItemDescription(self, menuitem, indent=0):
        spaces       = ' ' * indent
        less_spaces  = ' ' * (indent-self.INDENT) if indent >= self.INDENT else ''
        short_spaces = ' ' * (self.INDENT-1)

        kind = menuitem.GetKind()

        if kind == wx.ITEM_SEPARATOR:
            return less_spaces + '-'*20 + '\n'

        disabled = '' if menuitem.IsEnabled() else ' (disabled)'

        submenu = menuitem.GetSubMenu()
        if submenu != None:
            return self.getMenuDescription(submenu, 
                            indent=indent+self.INDENT, disabled=disabled)

        label = menuitem.GetItemLabelText() + disabled

        if kind == wx.ITEM_CHECK:
            check = 'x' if menuitem.IsChecked() else '-'
            return less_spaces + check + short_spaces + label + '\n'

        if kind == wx.ITEM_RADIO:
            radio = '.' if menuitem.IsChecked() else 'o'
            return less_spaces + radio + short_spaces + label + '\n'

        return spaces + label + '\n'   # ITEM_NORMAL



if __name__ == "__main__":
    app = MyApp(False)
#    wx.lib.inspection.InspectionTool().Show()  # widget inspection tool
    app.MainLoop()

# end mymenu.py

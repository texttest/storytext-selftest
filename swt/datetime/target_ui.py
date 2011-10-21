from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *

shell = Shell()
shell.setLayout(GridLayout(2, False))

menubar = Menu(shell, SWT.BAR)
shell.setMenuBar(menubar)
fileItem = MenuItem(menubar, SWT.CASCADE)
fileItem.setText("&File")
submenu = Menu(shell, SWT.DROP_DOWN)
fileItem.setMenu(submenu)
itemRedraw = MenuItem(submenu, SWT.PUSH)
itemRedraw.setText("Redraw!")

calendar = DateTime(shell, SWT.CALENDAR)
calendar.setData("org.eclipse.swtbot.widget.key", "The Calendar")
# Month starts from 0, oh yes!
calendar.setDate(1975, 1, 18)
gridData = GridData()
gridData.horizontalSpan = 2
calendar.setLayoutData(gridData)

date = DateTime(shell, SWT.DATE)
date.setData("org.eclipse.swtbot.widget.key", "The Date")
date.setDate(1976, 1, 3)

time = DateTime(shell, SWT.TIME | SWT.SHORT)
time.setData("org.eclipse.swtbot.widget.key", "The Time")
time.setTime(14, 0, 0)
    
class PrintListener(Listener):
    def handleEvent(self, e):
        print "Calendar changed"

class PrintListener2(Listener):
    def handleEvent(self, e):
        print "Time changed"

class PrintListener3(Listener):
    def handleEvent(self, e):
        print "Date changed"
        
class RedrawListener(Listener):
    def handleEvent(self, e):
        text = date.getChildren()[0]
        text.redraw()
        text.update()
        
itemRedraw.addListener(SWT.Selection, RedrawListener())

calendar.addListener(SWT.Selection, PrintListener())
time.addListener(SWT.Selection, PrintListener2())
date.addListener(SWT.Selection, PrintListener3())

shell.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

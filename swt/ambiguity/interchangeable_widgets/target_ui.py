from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell, Menu, MenuItem, ToolBar, ToolItem, Button, Listener

def addItem(i, item, name):
    item.setText(name + " item " + str(i))
    class PrintListener(Listener):
        def handleEvent(self, e):
            print "Selected item", i, e.widget.__class__.name

    item.addListener(SWT.Selection, PrintListener())

shell = Shell()
menuBar = Menu(shell, SWT.BAR)
shell.setMenuBar(menuBar)
fileItem = MenuItem(menuBar, SWT.CASCADE)
fileItem.setText("&File")
submenu = Menu(shell, SWT.DROP_DOWN)
fileItem.setMenu(submenu)
for i in range(1, 4):
    addItem(i, MenuItem(submenu, SWT.PUSH), "Menu")

bar = ToolBar(shell, SWT.BORDER)
for i in range(1, 4):
    addItem(i, ToolItem(bar, SWT.PUSH), "Toolbar")
        
bar.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

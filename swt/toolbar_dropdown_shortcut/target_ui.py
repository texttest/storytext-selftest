from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *

def addItem(i, menu):
    item = MenuItem(menu, SWT.PUSH)
    item.setText("Item " + str(i))
    class PrintListener(Listener):
        def handleEvent(self, e):
            print "Selected item", i
            
    item.addListener(SWT.Selection, PrintListener())

shell = Shell()

toolBar = ToolBar(shell, SWT.NONE)

clientArea = shell.getClientArea()
toolBar.setLocation(clientArea.x, clientArea.y)
menu = Menu(shell, SWT.POP_UP)
for i in range(8):
    addItem(i, menu)

item = ToolItem(toolBar, SWT.DROP_DOWN)
item.setText("Drop Down")
class MenuListener(Listener):
    def handleEvent(self, event):
        if event.detail == SWT.ARROW:
            rect = item.getBounds()
            pt = Point(rect.x, rect.y + rect.height)
            pt = toolBar.toDisplay(pt)
            menu.setLocation(pt.x, pt.y)
            menu.setVisible(True)
        else:
            print "Pressed the normal button..."

item.addListener(SWT.Selection, MenuListener())
toolBar.pack()
shell.pack()
shell.setSize(100, 100)
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

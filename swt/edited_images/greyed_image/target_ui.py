from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Shell, ToolBar, ToolItem, Menu, MenuItem, Listener
from org.eclipse.swt.graphics import Point, Image

def addItem(i, menu):
    item = MenuItem(menu, SWT.PUSH)
    item.setText("Item " + str(i))
    class PrintListener(Listener):
        def handleEvent(self, e):
            print "Selected item", i
            
    item.addListener(SWT.Selection, PrintListener())
    return item

shell = Shell()

toolBar = ToolBar(shell, SWT.NONE)

clientArea = shell.getClientArea()
toolBar.setLocation(clientArea.x, clientArea.y)
menu = Menu(shell, SWT.POP_UP)
menuItem =  addItem(1, menu)
img = Image(shell.getDisplay(), "icons/copy_edit.gif")
menuItem.setImage(Image(shell.getDisplay(), img, SWT.IMAGE_GRAY))
addItem(2, menu)

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

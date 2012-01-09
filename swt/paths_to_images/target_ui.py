from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import Image

def addItems(bar, display):
    item1 = ToolItem(bar, SWT.PUSH)
    item1.setText("Copy")
    item1.setImage(Image(display, "icons1/copy_edit.gif"))

    item2 = ToolItem(bar, SWT.PUSH)
    item2.setText("Paste")
    item2.setImage(Image(display, "icons1/others/paste_edit.gif"))

    item3 = ToolItem(bar, SWT.PUSH)
    item3.setText("Save")
    item3.setImage(Image(display, "icons2/save_edit.gif"))

#    class PrintListener(Listener):
#        def handleEvent(self, e):
#            print "Selected item", i
#            newItem = ToolItem(bar, SWT.PUSH)
#            newItem.setText("Extra Item " + str(i))
#            bar.pack()

#    item.addListener(SWT.Selection, PrintListener())

shell = Shell()
bar = ToolBar(shell, SWT.BORDER)
addItems(bar, shell.getDisplay())
        
bar.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

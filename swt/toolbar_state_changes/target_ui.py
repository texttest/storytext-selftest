from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Shell, ToolBar, ToolItem, Listener

def addItem(i, bar):
    item = ToolItem(bar, SWT.PUSH)
    item.setText("Item " + str(i))
    class PrintListener(Listener):
        def handleEvent(self, e):
            print "Selected item", i
            e.widget.setEnabled(not e.widget.isEnabled())

    item.addListener(SWT.Selection, PrintListener())

shell = Shell()
bar = ToolBar(shell, SWT.BORDER)
for i in range(1, 8):
    addItem(i, bar)
        
bar.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

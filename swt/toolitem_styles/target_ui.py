from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Shell, ToolBar, ToolItem, Listener

styles = {"SWT.PUSH":SWT.PUSH, "SWT.CHECK":SWT.CHECK, "SWT.RADIO":SWT.RADIO, "WT.DROP_DOWN":SWT.DROP_DOWN}

def addItem(i, name, style, bar):
    item = ToolItem(bar, style)
    item.setText("Item " + str(i))
    class PrintListener(Listener):
        def handleEvent(self, e):
            print "Selected item", i, "Style", name
            newItem = ToolItem(bar, style)
            newItem.setText("Extra Item " + str(i))
            bar.pack()

    item.addListener(SWT.Selection, PrintListener())

shell = Shell()
bar = ToolBar(shell, SWT.BORDER)
for i, (name, style)  in enumerate(styles.items()):
    addItem(i + 1, name, style,  bar)

addItem(5, "SWT.SEPARATOR", SWT.SEPARATOR, bar)   
bar.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

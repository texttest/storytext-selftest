from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *

shell = Shell()
swtlist = List(shell, SWT.BORDER | SWT.V_SCROLL)
for i in range(10):
    swtlist.add("Item " + str(i))

class PrintListener(Listener):
    def handleEvent(self, e):
        print "Selection = " + repr(list(swtlist.getSelectionIndices()))

swtlist.setBounds(0, 0, 100, 100)   
swtlist.addListener(SWT.Selection, PrintListener())

shell.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

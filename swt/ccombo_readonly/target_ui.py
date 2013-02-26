from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *
from org.eclipse.swt.custom import CCombo

shell = Shell()
combo = CCombo(shell, SWT.BORDER | SWT.READ_ONLY)
combo.setItems(["", "Alpha", "Bravo", "Charlie" ])
combo.setText("")
combo.setSize(100, 100)

class PrintListener(Listener):
    def handleEvent(self, e):
        print "Selection =", combo.getSelectionIndex()

combo.addListener(SWT.Selection, PrintListener())

shell.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

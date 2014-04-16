from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Shell, Listener
from org.eclipse.swt.custom import CCombo

shell = Shell()
combo = CCombo(shell, SWT.BORDER)
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

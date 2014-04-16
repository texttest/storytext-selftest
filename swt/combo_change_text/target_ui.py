from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Shell, Combo, Listener

shell = Shell()
combo = Combo(shell, SWT.READ_ONLY)
combo.setItems([ "Alpha", "Bravo", "Charlie" ])
combo.setText("Alpha")
combo.setSize(100, 10)

class PrintListener(Listener):
    def handleEvent(self, e):
        ix = combo.getSelectionIndex()
        newText = "Selected " + combo.getItem(ix)
        combo.setItem(ix, newText)
        combo.setText(newText)

combo.addListener(SWT.Selection, PrintListener())

shell.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Button, Listener, Shell
from org.eclipse.swt.layout import GridLayout

shell = Shell()
image = shell.getDisplay().getSystemImage(SWT.ICON_QUESTION)
layout = GridLayout(2, False)
shell.setLayout(layout)
button = Button(shell, SWT.PUSH)
button.setImage(image)
button.setText("Why?")

class PrintListener(Listener):
    def handleEvent(self, e):
        print "Because."
        button2.setEnabled(True)

button.addListener(SWT.Selection, PrintListener())

button2 = Button(shell, SWT.PUSH)
button2.setText("Exit")
button2.setEnabled(False)

class CloseListener(Listener):
    def handleEvent(self, e):
        shell.close()


button2.addListener(SWT.Selection, CloseListener())

shell.setSize(200, 200)
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *

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

button.addListener(SWT.Selection, PrintListener())

button2 = Button(shell, SWT.PUSH)
button2.setText("Exit")

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

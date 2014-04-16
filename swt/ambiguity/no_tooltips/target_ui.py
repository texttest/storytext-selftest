from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell, Button, Listener
from org.eclipse.swt.layout import GridLayout

shell = Shell()
image = shell.getDisplay().getSystemImage(SWT.ICON_WARNING)
layout = GridLayout(2, False)
shell.setLayout(layout)
button = Button(shell, SWT.PUSH)
button.setImage(image)
button.setText("Button")

class PreferredPrintListener(Listener):
    def handleEvent(self, e):
        print "Right!"

button.addListener(SWT.Selection, PreferredPrintListener())

button2 = Button(shell, SWT.PUSH)
button2.setText("Button")

class PrintListener(Listener):
    def handleEvent(self, e):
        print "Wrong!"

button2.addListener(SWT.Selection, PrintListener())

shell.setSize(200, 200)
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

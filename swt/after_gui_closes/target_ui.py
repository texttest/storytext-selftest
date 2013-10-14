from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *

shell = Shell()
layout = GridLayout(2, False)
shell.setLayout(layout)
button = Button(shell, SWT.CHECK)
button.setText("first")
button.setSelection(True)
button2 = Button(shell, SWT.CHECK)
button2.setText("second")

class PrintListener(Listener):
    def handleEvent(self, e):
        if e.widget.getSelection():
            print "Selected the", e.widget.getText(), "button."

button.addListener(SWT.Selection, PrintListener())
button2.addListener(SWT.Selection, PrintListener())

shell.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

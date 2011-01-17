from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *

shell = Shell()

class ConfirmListener(Listener):
    def handleEvent(self, e):
        style = SWT.DIALOG_TRIM | SWT.APPLICATION_MODAL
        messageBox = Shell(shell, style)
        messageBox.setText("Information")
        layout = GridLayout()
        messageBox.setLayout(layout)
        label = Label(messageBox, SWT.NONE)
        label.setText("You're exiting!")
        button = Button(messageBox, SWT.PUSH)
        button.setText("OK")
        class CloseListener(Listener):
            def handleEvent(self, e):
                messageBox.close()
        button.addListener(SWT.Selection, CloseListener())
        messageBox.open()
        messageBox.pack()
        display = messageBox.getDisplay()
        while not messageBox.isDisposed():
            if not display.readAndDispatch():
                display.sleep()

shell.setText("Main Window")
shell.addListener(SWT.Close, ConfirmListener())

shell.setSize(200, 200)
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

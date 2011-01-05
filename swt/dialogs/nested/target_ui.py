from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *

shell = Shell()

class SubDialogListener(Listener):
    def handleEvent(self, e):
        style = SWT.DIALOG_TRIM | SWT.APPLICATION_MODAL
        messageBox = Shell(shell, style)
        messageBox.setText("Second Dialog")
        button = Button(messageBox, SWT.NONE)
        button.setText("Close")
        class CloseListener(Listener):
            def handleEvent(self, e):
                messageBox.close()
        button.addListener(SWT.Selection, CloseListener())
        button.pack()
        messageBox.open()
        messageBox.pack()
        display = messageBox.getDisplay()
        while not messageBox.isDisposed():
            if not display.readAndDispatch():
                display.sleep()

class DialogListener(Listener):
    def handleEvent(self, e):
        style = SWT.DIALOG_TRIM | SWT.APPLICATION_MODAL
        messageBox = Shell(shell, style)
        messageBox.setText("First Dialog")
        text = Text(messageBox, SWT.NONE)
        text.pack()
        button = Button(messageBox, SWT.NONE)
        button.setText("Open another dialog")
        button.addListener(SWT.Selection, SubDialogListener())
        button.pack()
        messageBox.open()
        messageBox.pack()
        display = messageBox.getDisplay()
        while not messageBox.isDisposed():
            if not display.readAndDispatch():
                display.sleep()

shell.setText("Main Window")
button = Button(shell, SWT.NONE)
button.setText("Open a dialog")
button.addListener(SWT.Selection, DialogListener())
button.pack()
shell.setSize(200, 200)
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

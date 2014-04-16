from java.lang import Runnable
from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell, Composite, Label, Text, Button, Listener, Event
from org.eclipse.swt.layout import GridLayout, FillLayout

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
        messageBox.pack()
        messageBox.open()
        display = messageBox.getDisplay()
        while not messageBox.isDisposed():
            if not display.readAndDispatch():
                display.sleep()

shell.setText("Main Window")
shell.setLayout(FillLayout())

composite = Composite(shell, SWT.NONE)
layout = GridLayout(2, False)
composite.setLayout(layout)

label = Label(composite, SWT.NONE)
label.setText("Name")
text = Text(composite, SWT.NONE)
label2 = Label(composite, SWT.NONE)
label2.setText("City")
text2 = Text(composite, SWT.NONE)

class AppEventRunnable(Runnable):
    def run(self):
        x = Event()
        x.text = "text update to complete"
        text.notifyListeners(1234, x)


class ModifyListener(Listener):
    def handleEvent(self, e):
        if e.widget.getText() == "xxx":
            shell.getDisplay().timerExec(1000, AppEventRunnable())

text.addListener(SWT.Modify, ModifyListener())
text2.addListener(SWT.Modify, ModifyListener())

shell.addListener(SWT.Close, ConfirmListener())

shell.setSize(200, 200)
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

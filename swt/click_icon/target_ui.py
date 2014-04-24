from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Shell, Label, Listener
from org.eclipse.swt.layout import FillLayout

shell = Shell()
display = shell.getDisplay()
shell.setLayout(FillLayout())
shell.setText("Icon Example")

label = Label(shell, SWT.NONE)
label.setImage(display.getSystemImage(SWT.ICON_QUESTION))
        
class MouseListener(Listener):
    def handleEvent(self, e):
        print "Clicked on the question!"
        
label.addListener(SWT.MouseDown, MouseListener())

shell.setSize(300, 300)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

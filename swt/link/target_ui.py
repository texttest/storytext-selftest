from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *

shell = Shell()
shell.setLayout(GridLayout(1, False))
image = shell.getDisplay().getSystemImage(SWT.ICON_QUESTION)
link = Link(shell, SWT.NONE)
link.setText('<a>Here is a link</a>')
link2 = Link(shell, SWT.NONE)
link2.setText('<a>Another link</a>')
link.pack()
link2.pack()

class PrintListener(Listener):
    def handleEvent(self, e):
        print "Selection: " + e.text

link.addListener(SWT.Selection, PrintListener())

class PrintListener2(Listener):
    def handleEvent(self, e):
        print "Second Selection: " + e.text

link2.addListener(SWT.Selection, PrintListener2())

shell.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

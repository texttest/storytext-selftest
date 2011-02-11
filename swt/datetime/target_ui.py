from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *

shell = Shell()
shell.setLayout(RowLayout())

calendar = DateTime(shell, SWT.CALENDAR)
calendar.setData("org.eclipse.swtbot.widget.key", "The Calendar")
# Month starts from 0, oh yes!
calendar.setDate(1975, 1, 18)
time = DateTime(shell, SWT.TIME)
time.setData("org.eclipse.swtbot.widget.key", "The Time")
time.setTime(4, 0, 0)
    
class PrintListener(Listener):
    def handleEvent(self, e):
        print "Calendar changed"

class PrintListener2(Listener):
    def handleEvent(self, e):
        print "TimeChanged"

calendar.addListener(SWT.Selection, PrintListener())
time.addListener(SWT.Selection, PrintListener2())

shell.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

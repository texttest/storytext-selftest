from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Shell, Spinner, Label
from org.eclipse.swt.layout import GridLayout

shell = Shell()

layout = GridLayout(2, False)
shell.setLayout(layout)

label = Label(shell, SWT.NONE)
label.setText("The Spinner")

spinner = Spinner(shell, SWT.BORDER)
spinner.setMinimum(0)
spinner.setMaximum(1000)
spinner.setSelection(500)
spinner.setIncrement(1)
spinner.setPageIncrement(100)

label.pack()
spinner.pack()
		
shell.pack()
shell.open()
display = shell.getDisplay()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

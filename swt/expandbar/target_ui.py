from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *

shell = Shell()
display = shell.getDisplay()
shell.setLayout(FillLayout())
shell.setText("ExpandBar Example")
bar = ExpandBar(shell, SWT.V_SCROLL)
image = display.getSystemImage(SWT.ICON_QUESTION)

# First item
composite = Composite(bar, SWT.NONE)
layout = GridLayout(2, False)
layout.marginLeft = layout.marginTop = layout.marginRight = layout.marginBottom = 10
layout.verticalSpacing = 10
composite.setLayout(layout)	
label = Label(composite, SWT.NONE)
label.setImage(display.getSystemImage(SWT.ICON_ERROR))
label = Label(composite, SWT.NONE)
label.setText("SWT.ICON_ERROR")
label = Label(composite, SWT.NONE)
label.setImage(display.getSystemImage(SWT.ICON_INFORMATION))
label = Label(composite, SWT.NONE)
label.setText("SWT.ICON_INFORMATION")
label = Label(composite, SWT.NONE)
label.setImage(display.getSystemImage(SWT.ICON_QUESTION))
label = Label(composite, SWT.NONE)
label.setText("SWT.ICON_QUESTION")
item1 = ExpandItem(bar, SWT.NONE, 0)
item1.setText("What is your favorite icon")
item1.setHeight(composite.computeSize(SWT.DEFAULT, SWT.DEFAULT).y)
item1.setControl(composite)
item1.setImage(image)
item1.setExpanded(True)

# Second item
composite = Composite(bar, SWT.NONE)
layout = GridLayout()
layout.marginLeft = layout.marginTop = layout.marginRight = layout.marginBottom = 10
layout.verticalSpacing = 10
composite.setLayout(layout)
button = Button(composite, SWT.PUSH)
button.setText("Button1")
button = Button(composite, SWT.PUSH)
button.setText("Button2")
item0 = ExpandItem(bar, SWT.NONE, 1)
item0.setText("What is your favorite button")
item0.setHeight(composite.computeSize(SWT.DEFAULT, SWT.DEFAULT).y)
item0.setControl(composite)
item0.setImage(image)

bar.setSpacing(8)
shell.setSize(400, 350)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

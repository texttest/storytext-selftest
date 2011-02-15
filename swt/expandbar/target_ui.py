from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *

shell = Shell()
display = shell.getDisplay()
shell.setLayout(FillLayout())
shell.setText("ExpandBar Example")

menubar = Menu(shell, SWT.BAR)
shell.setMenuBar(menubar)
fileItem = MenuItem(menubar, SWT.CASCADE)
fileItem.setText("&File")
submenu = Menu(shell, SWT.DROP_DOWN)
fileItem.setMenu(submenu)
item = MenuItem(submenu, SWT.PUSH)
item.setText("New ExpandItem")

bar = ExpandBar(shell, SWT.V_SCROLL)
image = display.getSystemImage(SWT.ICON_QUESTION)

# First item
composite = Composite(bar, SWT.NONE)
# Add a context menu, check we describe it properly
popupmenu = Menu(shell, SWT.POP_UP)
popupitem = MenuItem(popupmenu, SWT.PUSH)
popupitem.setText("Popup")
composite.setMenu(popupmenu)
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
item1 = ExpandItem(bar, SWT.NONE)
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
item0 = ExpandItem(bar, SWT.NONE)
item0.setText("What is your favorite button")
item0.setHeight(composite.computeSize(SWT.DEFAULT, SWT.DEFAULT).y)
item0.setControl(composite)
item0.setImage(image)

        
class AddListener(Listener):
    def handleEvent(self, e):
        item2 = ExpandItem(bar, SWT.NONE)
        composite = Composite(bar, SWT.NONE)
        layout = GridLayout(2, False)
        composite.setLayout(layout)

        label = Label(composite, SWT.NONE)
        label.setText("What is your name?")
        # Just to see if this fools the text-finding algorithm
        pointlessComposite = Composite(composite, SWT.NONE)
        text = Text(pointlessComposite, SWT.NONE)
        item2.setText("New Question")
        composite.pack()
        size = composite.computeSize(SWT.DEFAULT, SWT.DEFAULT)
        item2.setHeight(size.y)
        item2.setControl(composite)
        item2.setImage(image)
        item2.setExpanded(True)
        
item.addListener(SWT.Selection, AddListener())

bar.setSpacing(8)
shell.setSize(400, 550)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

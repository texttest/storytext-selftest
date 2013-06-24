## /*******************************************************************************
##  * Copyright (c) 2000, 2004 IBM Corporation and others.
##  * All rights reserved. This program and the accompanying materials
##  * are made available under the terms of the Eclipse Public License v1.0
##  * which accompanies this distribution, and is available at
##  * http://www.eclipse.org/legal/epl-v10.html
##  *
##  * Contributors:
##  *     IBM Corporation - initial API and implementation
##  *******************************************************************************/
## /*
##  * Tree example snippet: create a tree
##  *
##  * For a list of all SWT example snippets see
##  * http://www.eclipse.org/swt/snippets/
## */
from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *
from org.eclipse.swt.custom import StackLayout

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

bar = Menu(shell, SWT.BAR)
shell.setMenuBar(bar)
fileItem = MenuItem(bar, SWT.CASCADE)
fileItem.setText("&File")
submenu = Menu(shell, SWT.DROP_DOWN)
fileItem.setMenu(submenu)
item = MenuItem(submenu, SWT.PUSH)
item.setText("Describe")

grid = Composite(shell, SWT.NONE)
layout = GridLayout(2, False)
grid.setLayout(layout)

labelFill = Composite(grid, SWT.NONE)
labelFill.setLayout(FillLayout())
labelGrid = Composite(labelFill, SWT.NONE)
labelGrid.setLayout(GridLayout(1, False))

textGrid = Composite(grid, SWT.NONE)
textGrid.setLayout(GridLayout(2, False))

label = Label(labelGrid, SWT.NONE)
label.setText("Names:")
name1 = Text(textGrid, SWT.NONE)
name1.setData("org.eclipse.swtbot.widget.key", "name1")
name2 = Text(textGrid, SWT.NONE)
name2.setData("org.eclipse.swtbot.widget.key", "name2")

label2 = Label(labelGrid, SWT.NONE)
label2.setText("Phone Numbers:")
phone1 = Text(textGrid, SWT.NONE)
phone1.setData("org.eclipse.swtbot.widget.key", "phone1")
phone2 = Text(textGrid, SWT.NONE)
phone2.setData("org.eclipse.swtbot.widget.key", "phone2")



shell.setSize(300, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

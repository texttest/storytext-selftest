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
from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell, Menu, MenuItem, Composite, Label, Text, Listener
from org.eclipse.swt.layout import FillLayout, GridLayout

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
item.setText("Show All")

composite = Composite(shell, SWT.NO_RADIO_GROUP)

# Extra level, just to make sure we can handle parent-of-parent checks
subComp = Composite(composite, SWT.NONE)
layout = GridLayout(2, False)
subComp.setLayout(layout)
label = Label(subComp, SWT.NONE | SWT.BORDER)
label.setText("Name")
label.setVisible(False)
text = Text(subComp, SWT.NONE)
subComp.pack()
composite.setVisible(False)

class ShowListener(Listener):
    def handleEvent(self, e):
        label.setVisible(True)
        composite.setVisible(True)
        
item.addListener(SWT.Selection, ShowListener())


shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

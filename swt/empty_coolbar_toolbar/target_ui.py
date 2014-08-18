##******************************************************************************
## Copyright (c) 2000, 2004 IBM Corporation and others.
## All rights reserved. This program and the accompanying materials
## are made available under the terms of the Eclipse Public License v1.0
## which accompanies this distribution, and is available at
## http://www.eclipse.org/legal/epl-v10.html
##
## Contributors:
##     IBM Corporation - initial API and implementation
## ******************************************************************************

##
## CoolBar example snippet: create a cool bar
##
## For a list of all SWT example snippets see
## http://www.eclipse.org/swt/snippets/
## 
from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell, Listener, Button, CoolItem, CoolBar, ToolBar, ToolItem
    

display = Display ()
shell = Shell(display)
bar = CoolBar(shell, SWT.NONE)

for i in range(3):
    item = CoolItem(bar, SWT.NONE)
    toolbar = ToolBar(bar, SWT.NONE)
    if i < 2:
        for j in range(2):
            toolitem = ToolItem(toolbar, SWT.PUSH)
            num = 2 * i + j
            toolitem.setText("Toolitem " + str(num))
    size = toolbar.computeSize(SWT.DEFAULT, SWT.DEFAULT)
    item.setPreferredSize(item.computeSize(size.x, size.y))
    item.setControl(toolbar)

clientArea = shell.getClientArea()
bar.setLocation(clientArea.x, clientArea.y)
bar.pack()

doubleemptybar = CoolBar(shell, SWT.NONE)
item = CoolItem(doubleemptybar, SWT.NONE)
emptytoolbar = ToolBar(doubleemptybar, SWT.NONE)
item.setControl(emptytoolbar)
doubleemptybar.pack()

emptybar = CoolBar(shell, SWT.NONE)
emptybar.pack()

shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

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
## Table example snippet: create a table (no columns, no headers)
##
## For a list of all SWT example snippets see
## http://www.eclipse.org/swt/snippets/
## 
from org.eclipse.swt import *
from org.eclipse.swt.graphics import Rectangle
from org.eclipse.swt.widgets import *

display = Display()
shell = Shell(display)
table = Table(shell, SWT.BORDER | SWT.V_SCROLL | SWT.H_SCROLL | SWT.MULTI)
for i in range(12):
    item = TableItem(table, 0)
    item.setText("Item " + str(i))

clientArea = shell.getClientArea()
table.setBounds(clientArea.x, clientArea.y, 100, 100)
shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

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
## ToolBar example snippet: place a combo box in a tool bar
##
## For a list of all SWT example snippets see
## http://www.eclipse.org/swt/snippets/
## 
from org.eclipse.swt import *
from org.eclipse.swt.graphics import Rectangle
from org.eclipse.swt.widgets import *

display = Display()
shell = Shell(display)
bar = ToolBar(shell, SWT.BORDER)
clientArea = shell.getClientArea()
bar.setLocation(clientArea.x, clientArea.y)

for i in range(4):
    item = ToolItem(bar, 0)
    item.setText("Item " + str(i))

sep = ToolItem(bar, SWT.SEPARATOR)
start = bar.getItemCount()
for i in range(start, start + 4):
    item = ToolItem(bar, 0)
    item.setText("Item " + str(i))

composite = Composite(bar, SWT.NONE)
combo = Combo(composite, SWT.READ_ONLY)
for i in range(4):
    combo.add("Item " + str(i))

combo.pack()
composite.pack()
sep.setWidth(combo.getSize().x)
sep.setControl(composite)
bar.pack()
shell.pack()
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch(): 
        display.sleep()

display.dispose()



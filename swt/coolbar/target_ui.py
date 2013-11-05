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
from org.eclipse.swt import *
from org.eclipse.swt.graphics import *
from org.eclipse.swt.widgets import *        
    

display = Display ()
shell = Shell (display)
bar = CoolBar (shell, SWT.BORDER)

class ClickListener(Listener):
    def __init__(self, num):
        self.num = num

    def handleEvent(self, e):
        bar.setBackground(display.getSystemColor(self.num))


for i in range(3):
    item = CoolItem(bar, SWT.NONE)
    button = Button(bar, SWT.PUSH)
    button.addListener(SWT.Selection, ClickListener(i + 3))
    button.setText("Button " + str(i))
    size = button.computeSize(SWT.DEFAULT, SWT.DEFAULT)
    item.setPreferredSize(item.computeSize(size.x, size.y))
    item.setControl(button)

clientArea = shell.getClientArea()
bar.setLocation(clientArea.x, clientArea.y)
bar.pack ()
shell.open ()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

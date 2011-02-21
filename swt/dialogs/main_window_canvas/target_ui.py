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

display = Display()
shell = Shell(display)
shell.setText("Main Window")

composite = Composite(shell, SWT.NONE)
composite.setLayout(FillLayout())

button = Button(composite, SWT.NONE)
button.setText("Show Dialog")

red = display.getSystemColor(SWT.COLOR_RED)
c = Canvas(composite, SWT.BORDER)
c.setBackground(red)
c.setFocus()
c.pack()

class DialogListener(Listener):
    def handleEvent(self, e):
        style = SWT.DIALOG_TRIM | SWT.APPLICATION_MODAL
        messageBox = Shell(shell, style)
        messageBox.setText("The Dialog")
        button = Button(messageBox, SWT.NONE)
        button.setText("Close")
        class CloseListener(Listener):
            def handleEvent(self, e):
                messageBox.close()
        button.addListener(SWT.Selection, CloseListener())
        button.pack()
        messageBox.setSize(200, 200)
        messageBox.open()
        display = messageBox.getDisplay()
        while not messageBox.isDisposed():
            if not display.readAndDispatch():
                display.sleep()
        
button.addListener(SWT.Selection, DialogListener())

composite.pack()
shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

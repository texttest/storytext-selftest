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
from java.lang import Runnable

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())


class DialogListener(Listener):
    def handleEvent(self, e):
        style = SWT.DIALOG_TRIM | SWT.APPLICATION_MODAL
        messageBox = Shell(shell, style)
        layout = GridLayout(2, False)
        messageBox.setLayout(layout)
        messageBox.setText("Dialog")
        dialogButton = Button(messageBox, SWT.NONE)
        dialogButton.setText("OK")
        class CloseListener(Listener):
            def handleEvent(lself, closeEvent):
                messageBox.close()

        dialogButton.addListener(SWT.Selection, CloseListener())
        messageBox.pack()
        messageBox.open()
        dialogDisplay = messageBox.getDisplay()
        while not messageBox.isDisposed():
            if not dialogDisplay.readAndDispatch():
                dialogDisplay.sleep()

class FilterListener(Listener):
    def __init__(self, button):
        self.button = button

    def handleEvent(self, event):
        class EventFinishedListener(Listener):
            def handleEvent(listenerSelf, e2): #@NoSelf
                if e2 is event:
                    x = Event()
                    x.text = "just before the dialog gets removed"
                    self.button.notifyListeners(1234, x)
        if event.widget is self.button:
            event.widget.addListener(SWT.Selection, EventFinishedListener())


        
shell.setText("Main Window")
button = Button(shell, SWT.NONE)
button.setText("Open a dialog")
listener = FilterListener(button)
display.addFilter(SWT.Selection, listener)
button.addListener(SWT.Selection, DialogListener())
button.pack()
shell.setSize(200, 200)

shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

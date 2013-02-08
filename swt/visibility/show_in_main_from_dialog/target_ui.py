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
composite = Composite(shell, SWT.NO_RADIO_GROUP)
layout = GridLayout(2, False)
composite.setLayout(layout)
button = Button(composite, SWT.NONE)
button.setText("Open a dialog")
mainLabel = Label(composite, SWT.NONE | SWT.BORDER)
mainLabel.setText("Just appeared!")
composite.pack()
mainLabel.setVisible(False)

class DialogListener(Listener):
    def handleEvent(self, e):
        style = SWT.DIALOG_TRIM | SWT.APPLICATION_MODAL
        dialog = Shell(shell, style)
        dialog.setText("The Dialog")
        dialog.setLayout(FillLayout())
        
        button = Button(dialog, SWT.NONE)
        button.setText("Show All")

        composite = Composite(dialog, SWT.NO_RADIO_GROUP)

        layout = GridLayout(2, False)
        composite.setLayout(layout)
        label = Label(composite, SWT.NONE | SWT.BORDER)
        label.setText("Name")
        label.setVisible(False)
        text = Text(composite, SWT.NONE)
        composite.pack()
        composite.setVisible(False)

        class ShowListener(Listener):
            def handleEvent(self, e):
                label.setVisible(True)
                composite.setVisible(True)
                mainLabel.setVisible(True)

        button.addListener(SWT.Selection, ShowListener())
        dialog.pack()
        dialog.open()
        display = dialog.getDisplay()
        while not dialog.isDisposed():
            if not display.readAndDispatch():
                display.sleep()

button.addListener(SWT.Selection, DialogListener())
shell.setSize(200, 290)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

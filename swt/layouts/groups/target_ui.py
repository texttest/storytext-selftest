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
from org.eclipse.swt.widgets import Display, Shell, Composite, Label, Text, Group, Listener
from org.eclipse.swt.layout import FillLayout, GridLayout

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

def addGroup(title, first, second):
    composite = Group(shell, SWT.NONE)
    composite.setText(title)
    layout = GridLayout(2, False)
    composite.setLayout(layout)

    label = Label(composite, SWT.NONE)
    label.setText(first)
    text = Text(composite, SWT.NONE)
    label2 = Label(composite, SWT.NONE)
    label2.setText(second)
    text2 = Text(composite, SWT.NONE)
    return composite, text

group1, text1 = addGroup("Personal", "First Name", "Surname")
addGroup("Corporate", "Employer", "Position")

class MyListener(Listener):
    def handleEvent(self, e):
        if "queen" in e.widget.getText().lower():
            group1.setText("Royal Titles")

text1.addListener(SWT.Modify, MyListener())

shell.setSize(500, 100)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

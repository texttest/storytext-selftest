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
from org.eclipse.swt.widgets import Display, Shell, Composite, Label, Text, Button, Listener
from org.eclipse.swt.layout import GridLayout, FillLayout, GridData
from org.eclipse.swt.custom import CLabel

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

composite = Composite(shell, SWT.NONE)
layout = GridLayout(2, False)
composite.setLayout(layout)

header =  CLabel(composite, SWT.NONE)
header.setText("Your details")
gridData = GridData()
# Eclipse thinks it's just fine to have spans greater than the number of columns
# Make sure we don't die as a result...
gridData.horizontalSpan = 3
header.setLayoutData(gridData)

label = CLabel(composite, SWT.NONE)
label.setText("Name")
text = Text(composite, SWT.NONE)
label2 = CLabel(composite, SWT.NONE)
label2.setText("City")
text2 = Text(composite, SWT.NONE)

shell.pack()
shell.setSize(500, 500)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

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
from org.eclipse.swt.widgets import Display, Shell, Menu, MenuItem, Composite, Label, Text, Button, Listener
from org.eclipse.swt.layout import FillLayout, GridLayout, RowLayout
from org.eclipse.swt.custom import StackLayout

display = Display()
shell = Shell(display)
shell.setBounds(10, 10, 300, 200)
#create the composite that the pages will share
contentPanel = Composite(shell, SWT.BORDER)
contentPanel.setBounds(100, 10, 190, 90)
layout = StackLayout()
contentPanel.setLayout(layout)

#create the first page's content
page0 = Composite(contentPanel, SWT.NONE)
page0.setLayout(RowLayout())
column0 = Composite(page0, SWT.NONE)
columnlayout = RowLayout()
columnlayout.type = SWT.VERTICAL
column0.setLayout(columnlayout)
label = Label(column0, SWT.NONE)
label.setText("(0, 0)")
label.pack()
label = Label(column0, SWT.NONE)
label.setText("(0, 1)")
label.pack()
column1 = Composite(page0, SWT.NONE)
column1.setLayout(columnlayout)
label = Label(column1, SWT.NONE)
label.setText("(1, 0)")
label.pack()
label = Label(column1, SWT.NONE)
label.setText("(1, 1)")
label.pack()
layout.topControl = page0

# create the second page's content	
page1 = Composite(contentPanel, SWT.NONE)
page1.setLayout(RowLayout())
text = Text(page1, SWT.NONE)
text.setText("Text on page 2")
text.pack()
contentPanel.layout()
text.setVisible(True)
page1.setVisible(True)

# create the button that will switch between the pages
pageButton = Button(shell, SWT.PUSH)
pageButton.setText("Push")
pageButton.setBounds(10, 10, 80, 25)

class FlipListener(Listener):
    def handleEvent(self, e):
        if layout.topControl is page0:
            layout.topControl = page1
        else:
            layout.topControl = page0
        contentPanel.layout()


pageButton.addListener(SWT.Selection, FlipListener())
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        text.setText("Something else")
        display.sleep()

display.dispose()

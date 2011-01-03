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
from org.eclipse.swt.custom import *

display = Display()
shell = Shell(display)
layout = FormLayout()
layout.marginWidth = 3
layout.marginHeight = 3
shell.setLayout(layout)

shell.setBounds(10, 10, 300, 200)

# create the button that will switch between the pages
pageButton = Button(shell, SWT.PUSH)
pageButton.setText("Push")
pageButton.setBounds(10, 10, 80, 25)
size = pageButton.computeSize(SWT.DEFAULT, SWT.DEFAULT)
pageButtonData = FormData(size.x, SWT.DEFAULT)
pageButtonData.right = FormAttachment(100, -4)
pageButtonData.bottom = FormAttachment(100, 0)
pageButton.setLayoutData(pageButtonData)

#create the composite that the pages will share
contentPanel = Composite(shell, SWT.BORDER)
contentPanel.setBounds(100, 10, 190, 90)
layout = StackLayout()
contentPanel.setLayout(layout)
size = contentPanel.computeSize(SWT.DEFAULT, SWT.DEFAULT)
contentPanelData = FormData(size.x, SWT.DEFAULT)
contentPanelData.left = FormAttachment(0, 0)
contentPanelData.right = FormAttachment(100, 0)
contentPanel.setLayoutData(contentPanelData)

#create the first page's content
page0 = Composite(contentPanel, SWT.NONE)
page0.setLayout(RowLayout())
label = Label(page0, SWT.NONE)
label.setText("First Page")
label.pack()
layout.topControl = page0

# create the second page's content	
page1 = Composite(contentPanel, SWT.NONE)
page1.setLayout(RowLayout())
contentPanel.layout()
page1.setVisible(True)

class FlipListener(Listener):
    def handleEvent(self, e):
        if layout.topControl is page0:
            text = Text(page1, SWT.NONE)
            text.setText("Text on page 2")
            text.pack()
            text.setVisible(True)
            layout.topControl = page1
        else:
            layout.topControl = page0
        contentPanel.layout()


pageButton.addListener(SWT.Selection, FlipListener())
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

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

import locale
from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell, Menu, MenuItem, Composite, Label, Text, Listener
from org.eclipse.swt.layout import FillLayout, GridLayout

encoding = locale.getdefaultlocale()[1]

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

bar = Menu(shell, SWT.BAR)
shell.setMenuBar(bar)
fileItem = MenuItem(bar, SWT.CASCADE)
fileItem.setText("&File")
submenu = Menu(shell, SWT.DROP_DOWN)
fileItem.setMenu(submenu)
item = MenuItem(submenu, SWT.PUSH)
item.setText("Describe")

composite = Composite(shell, SWT.NONE)
layout = GridLayout(2, False)
composite.setLayout(layout)

label = Label(composite, SWT.NONE)
label.setText("Name")
text = Text(composite, SWT.NONE)
text.setData("org.eclipse.swtbot.widget.key", "text1")
label2 = Label(composite, SWT.NONE)
label2.setText("City")
text2 = Text(composite, SWT.NONE)
text2.setData("org.eclipse.swtbot.widget.key", "text2")


class PrintListener(Listener):
    def handleEvent(self, e):
        unicodeText = "You are " + text.getText() + " and you live in " + text2.getText()
        print unicodeText.encode(encoding, 'replace')
        
item.addListener(SWT.Selection, PrintListener())


shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

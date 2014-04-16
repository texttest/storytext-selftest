
""" Copyright (c) 2000, 2004 IBM Corporation and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *
 * Contributors:
 *     IBM Corporation - initial API and implementation

 * Menu example snippet: create a bar and pull down menu (accelerators, mnemonics)
 *
 * For a list of all SWT example snippets see
 * http://www.eclipse.org/swt/snippets/ """

from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell, Composite, Label, Menu, MenuItem, Listener
from org.eclipse.swt.layout import GridLayout, GridData

display = Display()
shell = Shell(display)

shell.setLayout(GridLayout(2, False))

class MyComposite(Composite):
    pass

c1 = Composite(shell, SWT.BORDER)
c1.setLayoutData(GridData(100, 100))
label = Label(c1, SWT.NONE)
label.setText("Left Panel")
label.pack()

c2 = MyComposite(shell, SWT.BORDER)
c2.setLayoutData(GridData(100, 100))
label = Label(c2, SWT.NONE)
label.setText("Right Panel")
label.pack()

menu = Menu(shell, SWT.POP_UP)
item = MenuItem(menu, SWT.PUSH)
item.setText("Popup")
c2.setMenu(menu)

class PrintListener(Listener):
    def handleEvent(self, e):
        label.setText("")
        print "Label emptied"

item.addListener(SWT.Selection, PrintListener())

shell.pack()
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

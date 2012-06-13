
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

from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *
from org.eclipse.swt.graphics import *

display = Display()
shell = Shell(display)

shell.setLayout(GridLayout(2, False))
c1 = Composite(shell, SWT.BORDER)
c1.setLayoutData(GridData(100, 100))
tree = Tree(c1, SWT.BORDER)
for i in range(4):
    iItem = TreeItem(tree, 0)
    iItem.setText("Initial - " + str(i))

treemenu = Menu(shell, SWT.POP_UP)
treemenuitem = MenuItem(treemenu, SWT.PUSH)
treemenuitem.setText("Where am I?")
tree.setMenu(treemenu)
tree.pack()

c2 = Composite(shell, SWT.BORDER)
c2.setLayoutData(GridData(100, 100))
label = Label(c2, SWT.NONE)
label.setText("Right Panel")
label.pack()

menu = Menu(shell, SWT.POP_UP)
item = MenuItem(menu, SWT.PUSH)
item.setText("Popup")
item.setEnabled(False)
c2.setMenu(menu)
menu2 = Menu(shell, SWT.POP_UP)
item2 = MenuItem(menu2, SWT.PUSH)
item2.setText("Popup")
item2.setEnabled(False)
label.setMenu(menu2)

class PrintListener(Listener):
    def handleEvent(self, e):
        label.setText("Right Panel Clicked!")
        print "Clicked menu"

class TreePrintListener(Listener):
    def handleEvent(self, e):
        print "In a tree!"
        item.setEnabled(True)
        item2.setEnabled(True)

item.addListener(SWT.Selection, PrintListener())
item2.addListener(SWT.Selection, PrintListener())
treemenuitem.addListener(SWT.Selection, TreePrintListener())

shell.pack()
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

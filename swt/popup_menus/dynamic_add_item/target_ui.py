
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
tree = Tree(c1, SWT.BORDER | SWT.MULTI)
for i in range(4):
    iItem = TreeItem(tree, 0)
    iItem.setText("Initial - " + str(i))

treemenu = Menu(shell, SWT.POP_UP)
treemenuitem = MenuItem(treemenu, SWT.PUSH)
treemenuitem.setText("Where am I?")
tree.setMenu(treemenu)
tree.pack()


class DynamicPrintListener(Listener):
    def handleEvent(self, e):
        print "Clicked the dynamic one!"

class ClickListener(Listener):
    def handleEvent(self, e):
        newItem = MenuItem(treemenu, SWT.PUSH)
        newItem.setText("Dynamic!")
        newItem.addListener(SWT.Selection, DynamicPrintListener())


tree.addListener(SWT.Selection, ClickListener())

shell.pack()
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

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
from org.eclipse.swt.widgets import Display, Shell, Tree, TreeItem, Menu, MenuItem, Listener
from org.eclipse.swt.layout import FillLayout

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
item.setText("New TreeItem")

tree = Tree(shell, SWT.BORDER)
for i in range(4):
    iItem = TreeItem(tree, 0)
    iItem.setText("Initial - " + str(i))

class TreeAddListener(Listener):
    def handleEvent(self, e):
        item = TreeItem(tree, 0)
        item.setText("Added - 0")

class PrintListener(Listener):
    def handleEvent(self, event):
        print event.type == SWT.DefaultSelection, event.item
        

tree.addListener(SWT.Selection, PrintListener())
tree.addListener(SWT.DefaultSelection, PrintListener())
        
item.addListener(SWT.Selection, TreeAddListener())


shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

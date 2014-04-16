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
from org.eclipse.swt.widgets import Display, Shell, Tree, TreeItem, TreeColumn, Listener
from org.eclipse.swt.layout import FillLayout

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

tree = Tree(shell, SWT.BORDER | SWT.H_SCROLL | SWT.V_SCROLL)
tree.setHeaderVisible(True)
column1 = TreeColumn(tree, SWT.LEFT)
column1.setText("Column 1")
column1.setWidth(200)
column2 = TreeColumn(tree, SWT.CENTER)
column2.setText("Column 2")
column2.setWidth(200)
column3 = TreeColumn(tree, SWT.RIGHT)
column3.setText("Column 3")
column3.setWidth(200)
for i in range(4):
    item = TreeItem(tree, SWT.NONE)
    item.setText([ "item " + str(i), "abc", "defghi" ])
    for j in range(4):
        subItem = TreeItem(item, SWT.NONE)
        subItem.setText([ "subitem " + str(j), "jklmnop", "qrs" ])
        
shell.pack()
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

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
from org.eclipse.swt.widgets import Display, Shell, Tree, TreeItem, Listener
from org.eclipse.swt.layout import FillLayout

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())
tree = Tree(shell, SWT.MULTI | SWT.BORDER | SWT.V_SCROLL | SWT.H_SCROLL)
for i in range(12):
    item = TreeItem(tree, SWT.NONE)
    if i == 0:
        item.setText("Initial Item,with commas")
    else:
        item.setText("Item " + str(i))

tree.setSize(100, 100)

class PrintListener(Listener):
    def handleEvent(self, event):
        print event.type == SWT.DefaultSelection, event.item
        

tree.addListener(SWT.Selection, PrintListener())
tree.addListener(SWT.DefaultSelection, PrintListener())
shell.setSize(200, 200)

shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

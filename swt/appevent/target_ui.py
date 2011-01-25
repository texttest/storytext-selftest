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
from java.lang import Runnable

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

tree = Tree(shell, SWT.BORDER)
for i in range(4):
    iItem = TreeItem(tree, 0)
    iItem.setText("Initial - " + str(i))


class TreeAddRunnable(Runnable):
    def run(self):
        if tree.isDisposed():
            return
        item = TreeItem(tree, 0)
        item.setText("Added - 0")
        x = Event()
        x.text = "row to be added"
        tree.notifyListeners(1234, x)

display.timerExec(3000, TreeAddRunnable())        

shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

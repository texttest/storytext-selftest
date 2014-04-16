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

from java.lang import Runnable
from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell, Tree, TreeItem, Listener, Event
from org.eclipse.swt.layout import FillLayout

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

class AddListener(Listener):
    def handleEvent(self, e):
        display.timerExec(1000, TreeAddRunnable())

tree.addListener(SWT.DefaultSelection, AddListener())

shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

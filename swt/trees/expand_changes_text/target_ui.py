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

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

class NameChangeListener(Listener):
    def handleEvent(self, e):
        e.item.setText(e.item.getText() + " - expanded!")

tree = Tree(shell, SWT.BORDER | SWT.MULTI)
for i in range(2):
    iItem = TreeItem(tree, 0)
    iItem.setText("Root " + str(i))
    for j in range(2):
        jItem = TreeItem(iItem, 0)
        jItem.setText("Branch " + str(i) + "." + str(j))

tree.addListener(SWT.Expand, NameChangeListener())

shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

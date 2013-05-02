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
from org.eclipse.swt.events import *
from org.eclipse.swt.custom import *
from org.eclipse.swt.graphics import *


display = Display()
shell = Shell(display)

shell.setLayout(FillLayout())
table = Table(shell, SWT.FULL_SELECTION | SWT.MULTI)
table.setLinesVisible(True)
table.setHeaderVisible(True)
column1 = TableColumn(table, SWT.NONE)
column1.setText("id")
column2 = TableColumn(table, SWT.NONE)
column2.setText("")
for i in range(9):
    item = TableItem(table, SWT.NONE)
    
column1.pack()
column2.pack()
	

tablemenu = Menu(shell, SWT.POP_UP)
tablemenuitem = MenuItem(tablemenu, SWT.PUSH)
tablemenuitem.setText("Add Data")
table.setMenu(tablemenu)
table.pack()

class AddDataListener(Listener):
    def handleEvent(self, event):
        for i, item in enumerate(table.getItems()):
            item.setText([ "item " + str(i), "edit this value" ])

tablemenuitem.addListener(SWT.Selection, AddDataListener())

shell.pack()
shell.setSize(500, 500)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

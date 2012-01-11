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
shell.setLayout(GridLayout())
table = Table(shell, SWT.MULTI | SWT.BORDER | SWT.FULL_SELECTION)
table.setLinesVisible(True)
table.setHeaderVisible(True)
table.setSortDirection(SWT.DOWN)
data = GridData(SWT.FILL, SWT.FILL, True, True)
data.heightHint = 200
table.setLayoutData(data)
titles = [ " ", "C", "!", "Description", "Resource", "In Folder", "Location" ]
for title in titles:
    column = TableColumn(table, SWT.NONE)
    column.setText(title)
    table.setSortColumn(column)

for i in range(10):
    item = TableItem(table, SWT.NONE)
    item.setText(0, "x")
    item.setText(1, "y")
    item.setText(2, "!")
    item.setText(3, "this stuff behaves the way I expect")
    item.setText(4, "almost everywhere")
    item.setText(5, "some.folder")
    item.setText(6, "line " + str(10 - i) + " in nowhere")
    
for i in range(len(titles)):
    table.getColumn(i).pack()

class SortListener(Listener):
    def handleEvent(self, e):
        items = table.getItems()
        column = e.widget
        index = table.getColumns().index(column)
        texts = [ item.getText(index) for item in items ]
        texts.sort()
        for i, item in enumerate(items):
            item.setText(index, texts[i])
        table.setSortColumn(column)

column.addListener(SWT.Selection, SortListener())

shell.pack()
shell.setSize(800, 500)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

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
from org.eclipse.swt.widgets import Display, Shell, Table, TableItem, TableColumn, Menu, MenuItem, Listener
from org.eclipse.swt.layout import GridLayout, GridData

display = Display()
shell = Shell(display)
shell.setLayout(GridLayout())

bar = Menu(shell, SWT.BAR)
shell.setMenuBar(bar)
fileItem = MenuItem(bar, SWT.CASCADE)
fileItem.setText("&File")
submenu = Menu(shell, SWT.DROP_DOWN)
fileItem.setMenu(submenu)
menuItem = MenuItem(submenu, SWT.PUSH)
menuItem.setText("Add Column")


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
    item.setText(3, "this description is unique but far too long to use as a key " + str(i))
    item.setText(4, "almost everywhere")
    item.setText(5, "some.folder")
    item.setText(6, "line " + str(10 - i) + " in nowhere")
    
for i in range(len(titles)):
    table.getColumn(i).pack()


class SortListener(Listener):
    def __init__(self):
        self.sortAsc = False

    def handleEvent(self, e):
        items = table.getItems()
        column = e.widget
        index = table.getColumns().index(column)
        texts = [ item.getText(index) for item in items ]
        texts.sort(reverse=self.sortAsc)
        for i, item in enumerate(items):
            item.setText(index, texts[i])
        table.setSortColumn(column)
        self.sortAsc = not self.sortAsc
        table.setSortDirection(SWT.UP if self.sortAsc else SWT.DOWN)

class AddColumnListener(Listener):
    def handleEvent(self, e):
        column = TableColumn(table, SWT.NONE)
        column.setText("Extra")
        for i, item in enumerate(table.getItems()):
            item.setText(7, "extra in line " + str(10 - i))
        column.pack()
        column.addListener(SWT.Selection, SortListener())
        table.setSortColumn(column)
        table.setSortDirection(SWT.DOWN)


for column in table.getColumns():
    column.addListener(SWT.Selection, SortListener())

menuItem.addListener(SWT.Selection, AddColumnListener())


shell.pack()
shell.setSize(800, 500)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

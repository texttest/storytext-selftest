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
column2.setText("info")
for i in range(10):
    item = TableItem(table, SWT.NONE)
    item.setText([ "item " + str(i), "edit this value" ])

column1.pack()
column2.pack()
	
editor = TableEditor(table)
#The editor must have the same size as the cell and must
#not be any smaller than 50 pixels.
editor.horizontalAlignment = SWT.LEFT
editor.grabHorizontal = True
editor.minimumWidth = 50


tablemenu = Menu(shell, SWT.POP_UP)
tablemenuitem = MenuItem(tablemenu, SWT.PUSH)
tablemenuitem.setText("Add Row")
table.setMenu(tablemenu)
table.pack()


class TableListener(Listener):
    def handleEvent(self, event):
        # Clean up any previous editor control
        oldEditor = editor.getEditor()
        if oldEditor is not None:
            oldEditor.dispose()
            
        # Identify the selected row
        item, column = self.findCell(event)
        if item is None:
            return
	
        # The control that will be the editor must be a child of the Table
        newEditor = Text(table, SWT.NONE)
        newEditor.setText(item.getText(column))
        class MyListener(Listener):
            def handleEvent(lself, me):
                if me.character == SWT.CR:
                    text = editor.getEditor()
                    text.setText(text.getText())
                    editor.getItem().setText(column, text.getText())
                    text.dispose()
        newEditor.addListener(SWT.KeyDown, MyListener())
        newEditor.selectAll()
        newEditor.setFocus()
        editor.setEditor(newEditor, item, column)

    def findCell(self, event):
        pt = Point(event.x, event.y)
        index = table.getTopIndex()
        for rowIndex in range(index, index + table.getItemCount()):
            item = table.getItem(rowIndex)
            for col in range(table.getColumnCount()):
                rect = item.getBounds(col)
                if rect.contains(pt):
                    return item, col
        return None, None

class AddRowListener(Listener):
    def handleEvent(self, event):
        item = TableItem(table, SWT.NONE)
        item.setText([ "extra item", "edit this value" ])
        
table.addListener(SWT.MouseDown, TableListener())
tablemenuitem.addListener(SWT.Selection, AddRowListener())

shell.pack()
shell.setSize(500, 500)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

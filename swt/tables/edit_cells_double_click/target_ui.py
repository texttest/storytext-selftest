##******************************************************************************
## Copyright (c) 2006, 2008 Tom Schindl and others.
## All rights reserved. This program and the accompanying materials
## are made available under the terms of the Eclipse Public License v1.0
## which accompanies this distribution, and is available at
## http://www.eclipse.org/legal/epl-v10.html
##
## Contributors:
##     Tom Schindl - initial API and implementation
## ******************************************************************************

from org.eclipse.jface.viewers import CellEditor
from org.eclipse.jface.viewers import ColumnLabelProvider
from org.eclipse.jface.viewers import ColumnViewerEditor
from org.eclipse.jface.viewers import ColumnViewerEditorActivationEvent
from org.eclipse.jface.viewers import ColumnViewerEditorActivationStrategy
from org.eclipse.jface.viewers import ICellModifier
from org.eclipse.jface.viewers import IStructuredContentProvider
from org.eclipse.jface.viewers import TableViewer
from org.eclipse.jface.viewers import TableViewerColumn
from org.eclipse.jface.viewers import TableViewerEditor
from org.eclipse.jface.viewers import TextCellEditor
from org.eclipse.jface.viewers import Viewer
from org.eclipse.swt import SWT
from org.eclipse.swt.layout import FillLayout
from org.eclipse.swt.widgets import Display
from org.eclipse.swt.widgets import Shell

##*
## Shows how to setup a Viewer to start cell editing on double click
##
## @author Tom Schindl <tom.schindl@bestsolution.at>
##
## 
class MyContentProvider(IStructuredContentProvider):
    def getElements(self, inputElement):
        return inputElement
		
    def dispose(self):
        pass
		
    def inputChanged(self, *args):
        pass

class MyModel:
    def __init__(self, counter):
        self.counter = counter
		
    def __repr__(self):
        return "Item " + str(self.counter)

def createModel():
    return map(MyModel, range(10))

flag = True
display = Display()

shell = Shell(display)
shell.setLayout(FillLayout())

v = TableViewer(shell, SWT.BORDER | SWT.FULL_SELECTION | SWT.MULTI)
v.setContentProvider(MyContentProvider())
v.setCellEditors([ TextCellEditor(v.getTable()),
                   TextCellEditor(v.getTable()),
                   TextCellEditor(v.getTable()) ])

class MyCellModifier(ICellModifier):
    def canModify(self, *args):
        return True
        
    def getValue(self, element, prop):
        return "Column " + prop + " => " + repr(element)

    def modify(self, element, prop, value):
        element.setText(int(prop) - 1, value)

v.setCellModifier(MyCellModifier())
v.setColumnProperties([ "1", "2", "3" ])

class MyStrategy(ColumnViewerEditorActivationStrategy):
    def isEditorActivationEvent(self, event):
        return event.eventType == ColumnViewerEditorActivationEvent.TRAVERSAL \
                              or event.eventType == ColumnViewerEditorActivationEvent.MOUSE_DOUBLE_CLICK_SELECTION \
                              or event.eventType == ColumnViewerEditorActivationEvent.PROGRAMMATIC
	
actSupport = MyStrategy(v)
TableViewerEditor.create(v, actSupport,
                         ColumnViewerEditor.TABBING_HORIZONTAL
                         | ColumnViewerEditor.TABBING_MOVE_TO_ROW_NEIGHBOR
                         | ColumnViewerEditor.TABBING_VERTICAL
                         | ColumnViewerEditor.KEYBOARD_ACTIVATION)

column = TableViewerColumn(v, SWT.NONE)
column.getColumn().setWidth(200)
column.getColumn().setMoveable(True)
column.getColumn().setText("Column 1")
column.setLabelProvider(ColumnLabelProvider())

column = TableViewerColumn(v, SWT.NONE)
column.getColumn().setWidth(200)
column.getColumn().setMoveable(True)
column.getColumn().setText("Column 2")
column.setLabelProvider(ColumnLabelProvider())

column = TableViewerColumn(v, SWT.NONE)
column.getColumn().setWidth(200)
column.getColumn().setMoveable(True)
column.getColumn().setText("Column 3")
column.setLabelProvider(ColumnLabelProvider())

model = createModel()
v.setInput(model)
v.getTable().setLinesVisible(True)
v.getTable().setHeaderVisible(True)
		
shell.open()

while (not shell.isDisposed()):
    if (not display.readAndDispatch()):
        display.sleep()
		

display.dispose()

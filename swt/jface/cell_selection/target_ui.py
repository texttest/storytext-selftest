##******************************************************************************
## Copyright (c) 2006, 2007 Tom Schindl and others.
## All rights reserved. This program and the accompanying materials
## are made available under the terms of the Eclipse Public License v1.0
## which accompanies this distribution, and is available at
## http://www.eclipse.org/legal/epl-v10.html
##
## Contributors:
##     Tom Schindl - initial API and implementation
## ******************************************************************************

from org.eclipse.jface.resource import FontRegistry
from org.eclipse.jface.viewers import CellEditor
from org.eclipse.jface.viewers import ColumnViewerEditor
from org.eclipse.jface.viewers import ColumnViewerEditorActivationEvent
from org.eclipse.jface.viewers import ColumnViewerEditorActivationStrategy
from org.eclipse.jface.viewers import FocusCellOwnerDrawHighlighter
from org.eclipse.jface.viewers import ICellModifier
from org.eclipse.jface.viewers import IStructuredContentProvider
from org.eclipse.jface.viewers import ITableColorProvider
from org.eclipse.jface.viewers import ITableFontProvider
from org.eclipse.jface.viewers import ITableLabelProvider
from org.eclipse.jface.viewers import LabelProvider
from org.eclipse.jface.viewers import TableViewer
from org.eclipse.jface.viewers import TableViewerEditor
from org.eclipse.jface.viewers import TableViewerFocusCellManager
from org.eclipse.jface.viewers import TextCellEditor
from org.eclipse.jface.viewers import Viewer
from org.eclipse.swt import SWT
from org.eclipse.swt.graphics import Color
from org.eclipse.swt.graphics import Font
from org.eclipse.swt.graphics import Image
from org.eclipse.swt.layout import FillLayout
from org.eclipse.swt.widgets import Display, Shell, Menu, MenuItem, Composite, Label, Text, TableColumn, Listener
from org.eclipse.swt.custom import TableCursor

##*
## Example usage of none mandatory interfaces of ITableFontProvider and
## ITableColorProvider
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
	

class MyLabelProvider(LabelProvider, ITableLabelProvider, ITableFontProvider, ITableColorProvider):
	def __init__(self):
                self.registry = FontRegistry()

	def getColumnImage(self, *args):
		pass

	def getColumnText(self, element, columnIndex):
		return "Column " + str(columnIndex) + " => " + repr(element)
	

	def getFont(self, element, columnIndex):
		if element.counter % 2 == 0:
			return self.registry.getBold(Display.getCurrent().getSystemFont().getFontData()[0].getName())	

	def getBackground(self, element, columnIndex):
		if element.counter % 2 == 0:
			return Display.getCurrent().getSystemColor(SWT.COLOR_RED)	

	def getForeground(self, element, columnIndex):
		if element.counter % 2 == 1:
			return Display.getCurrent().getSystemColor(SWT.COLOR_RED)


def addWidgets(shell):
	v = TableViewer(shell, SWT.BORDER|SWT.MULTI|SWT.FULL_SELECTION)
	v.setLabelProvider(MyLabelProvider())
	v.setContentProvider(MyContentProvider())

	v.setCellEditors([ TextCellEditor(v.getTable()), TextCellEditor(v.getTable()) ])
	class MyCellModifier(ICellModifier):
		def canModify(self, *args):
			return True
		

		def getValue(self, element, property):
			return "Column " + property + " => " + repr(element)
		

		def modify(self, *args):
                        pass
				
	v.setCellModifier(MyCellModifier())
	
	v.setColumnProperties([ "1","2" ])
	
	focusCellManager = TableViewerFocusCellManager(v, FocusCellOwnerDrawHighlighter(v))
	class MyColumnViewerEditorActivationStrategy(ColumnViewerEditorActivationStrategy):
		def isEditorActivationEvent(self, event):
			return event.eventType == ColumnViewerEditorActivationEvent.TRAVERSAL or \
                            event.eventType == ColumnViewerEditorActivationEvent.MOUSE_DOUBLE_CLICK_SELECTION or \
                            (event.eventType == ColumnViewerEditorActivationEvent.KEY_PRESSED and event.keyCode == SWT.CR) or \
                            event.eventType == ColumnViewerEditorActivationEvent.PROGRAMMATIC
		
	actSupport = MyColumnViewerEditorActivationStrategy(v)
	
	TableViewerEditor.create(v, focusCellManager, actSupport, ColumnViewerEditor.TABBING_HORIZONTAL
			| ColumnViewerEditor.TABBING_MOVE_TO_ROW_NEIGHBOR
			| ColumnViewerEditor.TABBING_VERTICAL | ColumnViewerEditor.KEYBOARD_ACTIVATION)

	
	column = TableColumn(v.getTable(), SWT.NONE)
	column.setWidth(200)
	column.setText("Column 1")

	column = TableColumn(v.getTable(), SWT.NONE)
	column.setWidth(200)
	column.setText("Column 2")

	model = createModel()
	v.setInput(model)
	v.getTable().setLinesVisible(True)
	v.getTable().setHeaderVisible(True)

        class SelectionListener(Listener):
                def handleEvent(self, e):
                        print "Selected", e.item
        v.getTable().addListener(SWT.Selection, SelectionListener())
                


def createModel():
	return map(MyModel, range(10))
 
display = Display()

shell = Shell(display)
shell.setLayout(FillLayout())
addWidgets(shell)
shell.open()

while (not shell.isDisposed()):
	if (not display.readAndDispatch()):
		display.sleep()


display.dispose()

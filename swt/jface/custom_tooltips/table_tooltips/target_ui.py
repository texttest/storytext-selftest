##******************************************************************************
## Copyright (c) 2006, 2007 Tom Schindl and others.
## All rights reserved. This program and the accompanying materials
## are made available under the terms of the Eclipse Public License v1.0
## which accompanies this distribution, and is available at
## http://www.eclipse.org/legal/epl-v10.html
##
## Contributors:
##     Tom Schindl - initial API and implementation
##     IBM - Improvement for Bug 159625 [Snippets] Update Snippet011CustomTooltips to reflect new API
## ******************************************************************************

from org.eclipse.jface.viewers import CellLabelProvider
from org.eclipse.jface.viewers import ColumnViewerToolTipSupport
from org.eclipse.jface.viewers import IStructuredContentProvider
from org.eclipse.jface.viewers import TableViewer
from org.eclipse.jface.viewers import TableViewerColumn
from org.eclipse.jface.viewers import Viewer
from org.eclipse.jface.viewers import ViewerCell
from org.eclipse.jface.window import ToolTip
from org.eclipse.swt import SWT
from org.eclipse.swt.graphics import Point
from org.eclipse.swt.layout import FillLayout
from org.eclipse.swt.widgets import Display
from org.eclipse.swt.widgets import Shell

##*
## Explore New API: JFace custom tooltips drawing.
## 
## @author Tom Schindl <tom.schindl@bestsolution.at>
## @since 3.3
## 

class MyContentProvider(IStructuredContentProvider):
    def getElements(self, inputElement):
        return [ "one", "two", "three", "four", "five", "six",
                 "seven", "eight", "nine", "ten" ]
    
    def dispose(self):
        pass

    def inputChanged(self, *args):
        pass

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

v = TableViewer(shell, SWT.FULL_SELECTION)
v.getTable().setLinesVisible(True)
v.getTable().setHeaderVisible(True)
v.setContentProvider(MyContentProvider())
ColumnViewerToolTipSupport.enableFor(v, ToolTip.NO_RECREATE)

class MyCellLabelProvider(CellLabelProvider):
    def getToolTipText(self, element):
        return "Tooltip (" + element + ")"
	
    def getToolTipShift(self, *args):
        return Point(5, 5)
	
    def getToolTipDisplayDelayTime(self, *args):
        return 100
	
    def getToolTipTimeDisplayed(self, *args):
        return 500
	
    def update(self, cell):
        cell.setText(cell.getElement())

labelProvider = MyCellLabelProvider()

column = TableViewerColumn(v, SWT.NONE)
column.setLabelProvider(labelProvider)
column.getColumn().setText("Column 1")
column.getColumn().setWidth(100)

v.setInput("")

shell.setText("Custom Tooltips")
shell.setSize(200, 200)
shell.open()

while (not shell.isDisposed()):
	if (not display.readAndDispatch()):
		display.sleep()
	
display.dispose()
	



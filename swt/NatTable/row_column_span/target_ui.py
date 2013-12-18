##******************************************************************************
## Copyright (c) 2012 Original authors and others.
## All rights reserved. This program and the accompanying materials
## are made available under the terms of the Eclipse Public License v1.0
## which accompanies this distribution, and is available at
## http://www.eclipse.org/legal/epl-v10.html
## 
## Contributors:
##     Original authors and others - initial API and implementation
## *****************************************************************************

from org.eclipse.nebula.widgets import nattable
from org.eclipse import swt
from java.util import Date

DATE_LABEL = "date_label"

class Person:
    properties = [ "id", "name", "birthDate" ]
    propertyToLabels = { "id" : "ID", "name": "First Name", "birthDate": "DOB"}
    def __init__(self, *args):
        self.args = args

    @classmethod
    def getLabels(cls):
        return map(cls.propertyToLabels.get, cls.properties)
	
class MyColumnHeaderProvider(nattable.data.IColumnPropertyAccessor):
    def getRowCount(self):
        return 1

    def getColumnCount(self):
        return 3

    def getDataValue(self, rowObj, colIndex):
        return rowObj[colIndex]


def createNatTable(parent):
    bodyDataProvider = setupBodyDataProvider()
    basicColHeaderProvider = nattable.data.ListDataProvider([ Person.getLabels() ], MyColumnHeaderProvider())
    colHeaderDataProvider = nattable.data.AutomaticSpanningDataProvider(basicColHeaderProvider, True, True)
        
    rowHeaderDataProvider = nattable.grid.data.DefaultRowHeaderDataProvider(bodyDataProvider)

    bodyLayer = BodyLayerStack(bodyDataProvider)
    columnHeaderLayer = ColumnHeaderLayerStack(colHeaderDataProvider, bodyLayer)
    rowHeaderLayer = RowHeaderLayerStack(rowHeaderDataProvider, bodyLayer)
    cornerDataProvider = nattable.grid.data.DefaultCornerDataProvider(colHeaderDataProvider, rowHeaderDataProvider)
    dataLayer = nattable.layer.DataLayer(cornerDataProvider)
    cornerLayer = nattable.grid.layer.CornerLayer(dataLayer, rowHeaderLayer, columnHeaderLayer)

    gridLayer = nattable.grid.layer.GridLayer(bodyLayer, columnHeaderLayer, rowHeaderLayer, cornerLayer)
    table = nattable.NatTable(parent, gridLayer, True)
    table.getConfigRegistry().registerConfigAttribute(nattable.config.CellConfigAttributes.DISPLAY_CONVERTER, 
                                                      nattable.data.convert.DefaultDateDisplayConverter(), 
                                                      nattable.style.DisplayMode.NORMAL, 
                                                      DATE_LABEL)
    return table

class MyPropAccessor(nattable.data.IColumnPropertyAccessor):
    def getColumnCount(self):
        return 3

    def getDataValue(self, rowObj, colIndex):
        return rowObj.args[colIndex]
	
    def setDataValue(self, rowObj, colIndex, newValue):
        print "Set, oops!"


def setupBodyDataProvider():
    people = [ Person(100, "Mickey Mouse", Date(1000000)), 
               Person(100, "Mickey Mouse", Date(1000000)), 
               Person(100, "Mickey Mouse", Date(1000000)), 
               Person(130, "Cartman", Date(3000000)), 
               Person(140, 140, Date(4000000)) ]
		
    return nattable.data.ListDataProvider(people, MyPropAccessor())


class MyLabelAccumulator(nattable.layer.cell.AbstractOverrider):
    def accumulateConfigLabels(self, configLabels, columnPosition, rowPosition):
        if columnPosition == 2:
            configLabels.addLabel(DATE_LABEL)

class BodyLayerStack(nattable.layer.AbstractLayerTransform):
    def __init__(self, dataProvider):
        spanningProvider = nattable.data.AutomaticSpanningDataProvider(dataProvider, True, True)
        bodyDataLayer = nattable.layer.SpanningDataLayer(spanningProvider)
        accumulator = MyLabelAccumulator()
        bodyDataLayer.setConfigLabelAccumulator(accumulator)
        columnReorderLayer = nattable.reorder.ColumnReorderLayer(bodyDataLayer)
        columnHideShowLayer = nattable.hideshow.ColumnHideShowLayer(columnReorderLayer)
        self.selectionLayer = nattable.selection.SelectionLayer(columnHideShowLayer)
        viewportLayer = nattable.viewport.ViewportLayer(self.selectionLayer)
        self.setUnderlyingLayer(viewportLayer)
		
    def getSelectionLayer(self):
        return self.selectionLayer
		

class ColumnHeaderLayerStack(nattable.layer.AbstractLayerTransform):
    def __init__(self, dataProvider, bodyLayer):
        spanningProvider = nattable.data.AutomaticSpanningDataProvider(dataProvider, True, True)
        dataLayer = nattable.layer.SpanningDataLayer(spanningProvider)
        colHeaderLayer = nattable.grid.layer.ColumnHeaderLayer(dataLayer, bodyLayer, bodyLayer.getSelectionLayer())
        self.setUnderlyingLayer(colHeaderLayer)
		
	

class RowHeaderLayerStack(nattable.layer.AbstractLayerTransform): 
    def __init__(self, dataProvider, bodyLayer):
        dataLayer = nattable.layer.DataLayer(dataProvider, 50, 20)
        rowHeaderLayer = nattable.grid.layer.RowHeaderLayer(dataLayer, bodyLayer, bodyLayer.getSelectionLayer())
        self.setUnderlyingLayer(rowHeaderLayer)

display = swt.widgets.Display()
shell = swt.widgets.Shell(display)
shell.setLayout(swt.layout.GridLayout())

class MyPaintListener(swt.widgets.Listener):
    def __init__(self):
        self.resized = False

    def handleEvent(self, e):
        if self.resized:
            return

        self.resized = True
        table = e.widget
        for i in range(table.getColumnCount()):
            columnCommand = nattable.resize.command.InitializeAutoResizeColumnsCommand(table, 
                                                                                       i, table.getConfigRegistry(), 
                                                                                       nattable.util.GCFactory(table))
            table.doCommand(columnCommand)
                
        for i in range(table.getRowCount()):
            rowCommand = nattable.resize.command.InitializeAutoResizeRowsCommand(table, 
                                                                                 i, table.getConfigRegistry(), 
                                                                                 nattable.util.GCFactory(table))
            table.doCommand(rowCommand)
    
        
table = createNatTable(shell)
data = swt.layout.GridData(swt.SWT.FILL, swt.SWT.FILL, True, True)
table.setLayoutData(data)
table.pack()

class MyLayerListener(nattable.layer.ILayerListener):
    def handleLayerEvent(self, e):
        if isinstance(e, nattable.selection.event.CellSelectionEvent):
            print "Clicked on cell labelled '" + str(table.getDataValueByPosition(e.getColumnPosition(), e.getRowPosition())) + "'"


table.addListener(swt.SWT.Paint, MyPaintListener())
table.addLayerListener(MyLayerListener())
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

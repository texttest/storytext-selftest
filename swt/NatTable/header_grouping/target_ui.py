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

from java.util import Date, TimeZone

from org.eclipse.nebula.widgets.nattable import NatTable
from org.eclipse.nebula.widgets.nattable.config import CellConfigAttributes
from org.eclipse.nebula.widgets.nattable.data import IColumnPropertyAccessor, ListDataProvider
from org.eclipse.nebula.widgets.nattable.data.convert import DefaultDateDisplayConverter
from org.eclipse.nebula.widgets.nattable.grid.data import DefaultColumnHeaderDataProvider, DefaultRowHeaderDataProvider, DefaultCornerDataProvider
from org.eclipse.nebula.widgets.nattable.grid.layer import CornerLayer, GridLayer, ColumnHeaderLayer, RowHeaderLayer
from org.eclipse.nebula.widgets.nattable.group import ColumnGroupHeaderLayer, ColumnGroupModel
from org.eclipse.nebula.widgets.nattable.hideshow import ColumnHideShowLayer
from org.eclipse.nebula.widgets.nattable.layer import DataLayer, AbstractLayerTransform, ILayerListener
from org.eclipse.nebula.widgets.nattable.layer.cell import AbstractOverrider
from org.eclipse.nebula.widgets.nattable.reorder import ColumnReorderLayer
from org.eclipse.nebula.widgets.nattable.resize.command import InitializeAutoResizeColumnsCommand, InitializeAutoResizeRowsCommand
from org.eclipse.nebula.widgets.nattable.selection import SelectionLayer
from org.eclipse.nebula.widgets.nattable.selection.event import CellSelectionEvent
from org.eclipse.nebula.widgets.nattable.style import DisplayMode
from org.eclipse.nebula.widgets.nattable.util import GCFactory
from org.eclipse.nebula.widgets.nattable.viewport import ViewportLayer

from org.eclipse.swt import SWT
from org.eclipse.swt.layout import GridLayout, GridData
from org.eclipse.swt.widgets import Display, Shell, Listener

DATE_LABEL = "date_label"

class Person:
    properties = [ "id", "name", "birthDate" ]
    propertyToLabels = { "id" : "ID", "name": "First Name", "birthDate": "DOB"}
    def __init__(self, *args):
        self.args = args

def createNatTable(parent):
    bodyDataProvider = setupBodyDataProvider()
    colHeaderDataProvider = DefaultColumnHeaderDataProvider(Person.properties, Person.propertyToLabels)
    rowHeaderDataProvider = DefaultRowHeaderDataProvider(bodyDataProvider)

    bodyLayer = BodyLayerStack(bodyDataProvider)
    columnHeaderLayer = ColumnHeaderLayerStack(colHeaderDataProvider, bodyLayer)
    columnGroupHeaderLayer = ColumnGroupHeaderLayer(columnHeaderLayer, bodyLayer.getSelectionLayer(), ColumnGroupModel())
    columnGroupHeaderLayer.addColumnsIndexesToGroup("Group 1", [ 1, 2 ])

    rowHeaderLayer = RowHeaderLayerStack(rowHeaderDataProvider, bodyLayer)
    cornerDataProvider = DefaultCornerDataProvider(colHeaderDataProvider, rowHeaderDataProvider)
    dataLayer = DataLayer(cornerDataProvider)
    cornerLayer = CornerLayer(dataLayer, rowHeaderLayer, columnGroupHeaderLayer)

    gridLayer = GridLayer(bodyLayer, columnGroupHeaderLayer, rowHeaderLayer, cornerLayer)
    table = NatTable(parent, gridLayer, True)
    CONVERTER = CellConfigAttributes.DISPLAY_CONVERTER
    NORMAL = DisplayMode.NORMAL
    tz = TimeZone.getTimeZone("GMT+1")
    dateConverter = DefaultDateDisplayConverter("yyyy-MM-dd HH:mm", tz)
    table.getConfigRegistry().registerConfigAttribute(CONVERTER, dateConverter, NORMAL, DATE_LABEL)
    return table

class MyPropAccessor(IColumnPropertyAccessor):
    def getColumnCount(self):
        return 3

    def getDataValue(self, rowObj, colIndex):
        return rowObj.args[colIndex]

    def setDataValue(self, rowObj, colIndex, newValue):
        print "Set, oops!"


def setupBodyDataProvider():
    people = [ Person(100, "Mickey Mouse", Date(1000000)), 
               Person(110, "Batman", Date(2000000)), 
               Person(120, "Bender", Date(3000000)), 
               Person(130, "Cartman", Date(4000000)), 
               Person(140, "Dogbert", Date(5000000)) ]
    return ListDataProvider(people, MyPropAccessor())


class MyLabelAccumulator(AbstractOverrider):
    def accumulateConfigLabels(self, configLabels, columnPosition, rowPosition):
        if columnPosition == 2:
            configLabels.addLabel(DATE_LABEL)

class BodyLayerStack(AbstractLayerTransform):
    def __init__(self, dataProvider):
        bodyDataLayer = DataLayer(dataProvider)
        accumulator = MyLabelAccumulator()
        bodyDataLayer.setConfigLabelAccumulator(accumulator)
        columnReorderLayer = ColumnReorderLayer(bodyDataLayer)
        columnHideShowLayer = ColumnHideShowLayer(columnReorderLayer)
        self.selectionLayer = SelectionLayer(columnHideShowLayer)
        viewportLayer = ViewportLayer(self.selectionLayer)
        self.setUnderlyingLayer(viewportLayer)

    def getSelectionLayer(self):
        return self.selectionLayer


class ColumnHeaderLayerStack(AbstractLayerTransform):
    def __init__(self, dataProvider, bodyLayer):
        dataLayer = DataLayer(dataProvider)
        colHeaderLayer = ColumnHeaderLayer(dataLayer, bodyLayer, bodyLayer.getSelectionLayer())
        self.setUnderlyingLayer(colHeaderLayer)

class RowHeaderLayerStack(AbstractLayerTransform): 
    def __init__(self, dataProvider, bodyLayer):
        dataLayer = DataLayer(dataProvider, 50, 20)
        rowHeaderLayer = RowHeaderLayer(dataLayer, bodyLayer, bodyLayer.getSelectionLayer())
        self.setUnderlyingLayer(rowHeaderLayer)

display = Display()
shell = Shell(display)
shell.setLayout(GridLayout())

class MyPaintListener(Listener):
    def __init__(self):
        self.resized = False

    def handleEvent(self, e):
        if self.resized:
            return

        self.resized = True
        table = e.widget
        for i in range(table.getColumnCount()):
            columnCommand = InitializeAutoResizeColumnsCommand(table, 
                                                               i, table.getConfigRegistry(), 
                                                               GCFactory(table))
            table.doCommand(columnCommand)
                
        for i in range(table.getRowCount()):
            rowCommand = InitializeAutoResizeRowsCommand(table, 
                                                         i, table.getConfigRegistry(), 
                                                         GCFactory(table))
            table.doCommand(rowCommand)
    
        
table = createNatTable(shell)
data = GridData(SWT.FILL, SWT.FILL, True, True)
table.setLayoutData(data)
table.pack()


table.addListener(SWT.Paint, MyPaintListener())
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

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

from org.eclipse.nebula.widgets.nattable import NatTable
from org.eclipse.nebula.widgets.nattable.config import AbstractRegistryConfiguration, DefaultNatTableStyleConfiguration, CellConfigAttributes, IEditableRule
from org.eclipse.nebula.widgets.nattable.data import IColumnPropertyAccessor, ListDataProvider
from org.eclipse.nebula.widgets.nattable.data.convert import DefaultBooleanDisplayConverter
from org.eclipse.nebula.widgets.nattable.edit import EditConfigAttributes
from org.eclipse.nebula.widgets.nattable.edit.editor import CheckBoxCellEditor, ComboBoxCellEditor
from org.eclipse.nebula.widgets.nattable.grid.data import DefaultColumnHeaderDataProvider, DefaultRowHeaderDataProvider, DefaultCornerDataProvider
from org.eclipse.nebula.widgets.nattable.grid.layer import CornerLayer, GridLayer, ColumnHeaderLayer, RowHeaderLayer
from org.eclipse.nebula.widgets.nattable.hideshow import ColumnHideShowLayer
from org.eclipse.nebula.widgets.nattable.layer import DataLayer, AbstractLayerTransform, ILayerListener
from org.eclipse.nebula.widgets.nattable.layer.cell import ColumnOverrideLabelAccumulator
from org.eclipse.nebula.widgets.nattable.painter.cell import CheckBoxPainter, ComboBoxPainter
from org.eclipse.nebula.widgets.nattable.reorder import ColumnReorderLayer
from org.eclipse.nebula.widgets.nattable.resize.command import InitializeAutoResizeColumnsCommand, InitializeAutoResizeRowsCommand
from org.eclipse.nebula.widgets.nattable.selection import SelectionLayer
from org.eclipse.nebula.widgets.nattable.selection.event import CellSelectionEvent
from org.eclipse.nebula.widgets.nattable.style import DisplayMode, HorizontalAlignmentEnum
from org.eclipse.nebula.widgets.nattable.util import GCFactory
from org.eclipse.nebula.widgets.nattable.viewport import ViewportLayer

from org.eclipse.swt import SWT
from org.eclipse.swt.layout import GridLayout, GridData
from org.eclipse.swt.widgets import Display, Shell, Listener

class Person:
    properties = [ "name", "married", "city" ]
    propertyToLabels = { "name": "First Name", "married" : "Married", "city": "City of Residence"}
    def __init__(self, *args):
        self.args = list(args)

def createNatTable(parent):
    bodyDataProvider = setupBodyDataProvider()
    colHeaderDataProvider = DefaultColumnHeaderDataProvider(Person.properties, Person.propertyToLabels)
    rowHeaderDataProvider = DefaultRowHeaderDataProvider(bodyDataProvider)

    bodyLayer = BodyLayerStack(bodyDataProvider)
    columnHeaderLayer = ColumnHeaderLayerStack(colHeaderDataProvider, bodyLayer)
    rowHeaderLayer = RowHeaderLayerStack(rowHeaderDataProvider, bodyLayer)
    cornerDataProvider = DefaultCornerDataProvider(colHeaderDataProvider, rowHeaderDataProvider)
    dataLayer = DataLayer(cornerDataProvider)
    cornerLayer = CornerLayer(dataLayer, rowHeaderLayer, columnHeaderLayer)

    gridLayer = GridLayer(bodyLayer, columnHeaderLayer, rowHeaderLayer, cornerLayer)
    natTable = NatTable(parent, gridLayer, False)
    defaultConfig = DefaultNatTableStyleConfiguration()
    defaultConfig.hAlign = HorizontalAlignmentEnum.LEFT
    natTable.addConfiguration(defaultConfig)
    natTable.addConfiguration(EditableGridConfiguration())
    natTable.configure()
    return natTable

class MyPropAccessor(IColumnPropertyAccessor):
    def getColumnCount(self):
        return 3

    def getDataValue(self, rowObj, colIndex):
        return rowObj.args[colIndex]

    def setDataValue(self, rowObj, colIndex, newValue):
        rowObj.args[colIndex] = newValue


def setupBodyDataProvider():
    people = [ Person("Joe", False, "London"),
               Person("Maria", True, "Santiago") ]

    return ListDataProvider(people, MyPropAccessor())

class BodyLayerStack(AbstractLayerTransform):
    def __init__(self, dataProvider):
        bodyDataLayer = DataLayer(dataProvider) 
        columnLabelAccumulator = ColumnOverrideLabelAccumulator(bodyDataLayer)
        bodyDataLayer.setConfigLabelAccumulator(columnLabelAccumulator)
        self.registerColumnLabels(columnLabelAccumulator)
        columnReorderLayer = ColumnReorderLayer(bodyDataLayer)
        columnHideShowLayer = ColumnHideShowLayer(columnReorderLayer)
        self.selectionLayer = SelectionLayer(columnHideShowLayer)
        viewportLayer = ViewportLayer(self.selectionLayer)
        self.setUnderlyingLayer(viewportLayer)

    def getSelectionLayer(self):
        return self.selectionLayer

    def registerColumnLabels(self, columnLabelAccumulator):
        columnLabelAccumulator.registerColumnOverrides(0, [ "name" ])
        columnLabelAccumulator.registerColumnOverrides(1, [ "married" ])
        columnLabelAccumulator.registerColumnOverrides(2, [ "city" ])

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

class EditableGridConfiguration(AbstractRegistryConfiguration):
    def configureRegistry(self, configRegistry):
        attrs = EditConfigAttributes
        cellattrs = CellConfigAttributes
        configRegistry.registerConfigAttribute(attrs.CELL_EDITABLE_RULE, IEditableRule.ALWAYS_EDITABLE)
        configRegistry.registerConfigAttribute(attrs.CELL_EDITOR, CheckBoxCellEditor(), 
                                               DisplayMode.EDIT, "married")
        configRegistry.registerConfigAttribute(cellattrs.CELL_PAINTER, CheckBoxPainter(), 
                                               DisplayMode.NORMAL, "married")
        configRegistry.registerConfigAttribute(cellattrs.DISPLAY_CONVERTER, DefaultBooleanDisplayConverter(), 
                                               DisplayMode.NORMAL, "married")

        comboBoxCellEditor = ComboBoxCellEditor([ "London", "Washington", "Santiago", "Stockholm" ])
        configRegistry.registerConfigAttribute(attrs.CELL_EDITOR, comboBoxCellEditor, DisplayMode.EDIT, "city")
        configRegistry.registerConfigAttribute(cellattrs.CELL_PAINTER, ComboBoxPainter(),
                                               DisplayMode.NORMAL, "city")

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

class MyLayerListener(ILayerListener):
    def handleLayerEvent(self, e):
        if isinstance(e, CellSelectionEvent):
            print "Clicked on cell labelled '" + str(table.getDataValueByPosition(e.getColumnPosition(), e.getRowPosition())) + "'"


table.addListener(SWT.Paint, MyPaintListener())
table.addLayerListener(MyLayerListener())
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

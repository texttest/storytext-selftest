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

class Person:
    properties = [ "name", "married", "city" ]
    propertyToLabels = { "name": "First Name", "married" : "Married", "city": "City of Residence"}
    def __init__(self, *args):
        self.args = list(args)
	

def createNatTable(parent):
    bodyDataProvider = setupBodyDataProvider()
    colHeaderDataProvider = nattable.grid.data.DefaultColumnHeaderDataProvider(Person.properties, Person.propertyToLabels)
    rowHeaderDataProvider = nattable.grid.data.DefaultRowHeaderDataProvider(bodyDataProvider)

    bodyLayer = BodyLayerStack(bodyDataProvider)
    columnHeaderLayer = ColumnHeaderLayerStack(colHeaderDataProvider, bodyLayer)
    rowHeaderLayer = RowHeaderLayerStack(rowHeaderDataProvider, bodyLayer)
    cornerDataProvider = nattable.grid.data.DefaultCornerDataProvider(colHeaderDataProvider, rowHeaderDataProvider)
    dataLayer = nattable.layer.DataLayer(cornerDataProvider)
    cornerLayer = nattable.grid.layer.CornerLayer(dataLayer, rowHeaderLayer, columnHeaderLayer)

    gridLayer = nattable.grid.layer.GridLayer(bodyLayer, columnHeaderLayer, rowHeaderLayer, cornerLayer)
    natTable = nattable.NatTable(parent, gridLayer, False)
    defaultConfig = nattable.config.DefaultNatTableStyleConfiguration()
    defaultConfig.hAlign = nattable.style.HorizontalAlignmentEnum.LEFT
    natTable.addConfiguration(defaultConfig)
    natTable.addConfiguration(EditableGridConfiguration())
    natTable.configure()
    return natTable

class MyPropAccessor(nattable.data.IColumnPropertyAccessor):
    def getColumnCount(self):
        return 3

    def getDataValue(self, rowObj, colIndex):
        return rowObj.args[colIndex]
	
    def setDataValue(self, rowObj, colIndex, newValue):
        rowObj.args[colIndex] = newValue


def setupBodyDataProvider():
    people = [ Person("Joe", False, "London"),
               Person("Maria", True, "Santiago") ]
		
    return nattable.data.ListDataProvider(people, MyPropAccessor())

	

class BodyLayerStack(nattable.layer.AbstractLayerTransform):
    def __init__(self, dataProvider):
        bodyDataLayer = nattable.layer.DataLayer(dataProvider) 
        columnLabelAccumulator = nattable.layer.cell.ColumnOverrideLabelAccumulator(bodyDataLayer)
        bodyDataLayer.setConfigLabelAccumulator(columnLabelAccumulator)
        self.registerColumnLabels(columnLabelAccumulator)
        columnReorderLayer = nattable.reorder.ColumnReorderLayer(bodyDataLayer)
        columnHideShowLayer = nattable.hideshow.ColumnHideShowLayer(columnReorderLayer)
        self.selectionLayer = nattable.selection.SelectionLayer(columnHideShowLayer)
        viewportLayer = nattable.viewport.ViewportLayer(self.selectionLayer)
        self.setUnderlyingLayer(viewportLayer)
		
    def getSelectionLayer(self):
        return self.selectionLayer
	
    def registerColumnLabels(self, columnLabelAccumulator):
        columnLabelAccumulator.registerColumnOverrides(0, "name");
        columnLabelAccumulator.registerColumnOverrides(1, "married");
        columnLabelAccumulator.registerColumnOverrides(2, "city");
	

class ColumnHeaderLayerStack(nattable.layer.AbstractLayerTransform):
    def __init__(self, dataProvider, bodyLayer):
        dataLayer = nattable.layer.DataLayer(dataProvider)
        colHeaderLayer = nattable.grid.layer.ColumnHeaderLayer(dataLayer, bodyLayer, bodyLayer.getSelectionLayer())
        self.setUnderlyingLayer(colHeaderLayer)
		
	

class RowHeaderLayerStack(nattable.layer.AbstractLayerTransform): 
    def __init__(self, dataProvider, bodyLayer):
        dataLayer = nattable.layer.DataLayer(dataProvider, 50, 20)
        rowHeaderLayer = nattable.grid.layer.RowHeaderLayer(dataLayer, bodyLayer, bodyLayer.getSelectionLayer())
        self.setUnderlyingLayer(rowHeaderLayer)

class EditableGridConfiguration(nattable.config.AbstractRegistryConfiguration):
    def configureRegistry(self, configRegistry):
        attrs = nattable.edit.EditConfigAttributes
        cellattrs = nattable.config.CellConfigAttributes
        IEditableRule = nattable.config.IEditableRule
        DisplayMode = nattable.style.DisplayMode
        configRegistry.registerConfigAttribute(attrs.CELL_EDITABLE_RULE, IEditableRule.ALWAYS_EDITABLE)
        configRegistry.registerConfigAttribute(attrs.CELL_EDITOR, nattable.edit.editor.CheckBoxCellEditor(), 
                                               DisplayMode.EDIT, "married")
        configRegistry.registerConfigAttribute(cellattrs.CELL_PAINTER, nattable.painter.cell.CheckBoxPainter(), 
                                               DisplayMode.NORMAL, "married")
        configRegistry.registerConfigAttribute(cellattrs.DISPLAY_CONVERTER, nattable.data.convert.DefaultBooleanDisplayConverter(), 
                                               DisplayMode.NORMAL, "married")

        comboBoxCellEditor = nattable.edit.editor.ComboBoxCellEditor([ "London", "Washington", "Santiago", "Stockholm" ])
        configRegistry.registerConfigAttribute(attrs.CELL_EDITOR, comboBoxCellEditor, DisplayMode.EDIT, "city")
        configRegistry.registerConfigAttribute(cellattrs.CELL_PAINTER, nattable.painter.cell.ComboBoxPainter(),
                                               DisplayMode.NORMAL, "city")

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

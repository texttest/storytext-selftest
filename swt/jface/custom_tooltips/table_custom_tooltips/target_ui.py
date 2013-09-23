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

from org.eclipse.jface.resource import ImageDescriptor
from org.eclipse.jface.resource import JFaceResources
from org.eclipse.jface.viewers import CellLabelProvider
from org.eclipse.jface.viewers import ColumnViewer
from org.eclipse.jface.viewers import ColumnViewerToolTipSupport
from org.eclipse.jface.viewers import IStructuredContentProvider
from org.eclipse.jface.viewers import TableViewer
from org.eclipse.jface.viewers import TableViewerColumn
from org.eclipse.jface.viewers import Viewer
from org.eclipse.jface.viewers import ViewerCell
from org.eclipse.jface.util import Policy
from org.eclipse.jface.window import ToolTip
from org.eclipse.swt import SWT
from org.eclipse.swt.browser import Browser
from org.eclipse.swt.graphics import Point
from org.eclipse.swt.layout import FillLayout
from org.eclipse.swt.layout import GridData
from org.eclipse.swt.layout import GridLayout
from org.eclipse.swt.widgets import Composite
from org.eclipse.swt.widgets import Display
from org.eclipse.swt.widgets import Event
from org.eclipse.swt.widgets import Shell
from org.eclipse.swt.widgets import Label
from org.eclipse.swt.widgets import Link

##*
## Explore New API: JFace custom tooltips drawing.
## 
## @author Tom Schindl <tom.schindl@bestsolution.at>
## @since 3.3
## '

class MyContentProvider(IStructuredContentProvider):
    def getElements(self, inputElement):
        return [ "one", "two", "three", "four" ]
    
    def dispose(self):
        pass

    def inputChanged(self, *args):
        pass
		
	

class FancyToolTipSupport(ColumnViewerToolTipSupport):
    headerText = "ToolTip-Header"

    HEADER_BG_COLOR = Policy.JFACE + ".TOOLTIP_HEAD_BG_COLOR"
    HEADER_FG_COLOR = Policy.JFACE + ".TOOLTIP_HEAD_FG_COLOR"
    HEADER_FONT = Policy.JFACE + ".TOOLTIP_HEAD_FONT"
    HEADER_CLOSE_ICON = Policy.JFACE + ".TOOLTIP_CLOSE_ICON"
    HEADER_HELP_ICON = Policy.JFACE + ".TOOLTIP_HELP_ICON"
    def createContentArea(self, parent, event):
        comp = Composite(parent,SWT.NONE)
        comp.setBackground(parent.getDisplay().getSystemColor(SWT.COLOR_INFO_BACKGROUND))
        layout = FillLayout()
        layout.marginWidth=5
        comp.setLayout(layout)
        l = Link(comp,SWT.NONE)
        l.setText(self.getText(event))
        l.setBackground(parent.getDisplay().getSystemColor(SWT.COLOR_INFO_BACKGROUND))
        return comp

    def createToolTipContentArea(self, event, parent):
        comp = Composite(parent,SWT.NONE)

        gl = GridLayout(1,False)
        gl.marginBottom=0
        gl.marginTop=0
        gl.marginHeight=0
        gl.marginWidth=0
        gl.marginLeft=0
        gl.marginRight=0
        gl.verticalSpacing=1
        comp.setLayout(gl)
        
        topArea = Composite(comp,SWT.NONE)
        data = GridData(SWT.FILL,SWT.FILL,True,False)
        data.widthHint=200
        topArea.setLayoutData(data)
        topArea.setBackground(JFaceResources.getColorRegistry().get(self.HEADER_BG_COLOR))

        gl = GridLayout(2,False)
        gl.marginBottom=2
        gl.marginTop=2
        gl.marginHeight=0
        gl.marginWidth=0
        gl.marginLeft=5
        gl.marginRight=2
        
        topArea.setLayout(gl)

        l = Label(topArea,SWT.NONE)
        l.setText(self.headerText)
        l.setBackground(JFaceResources.getColorRegistry().get(self.HEADER_BG_COLOR))
        l.setFont(JFaceResources.getFontRegistry().get(self.HEADER_FONT))
        l.setForeground(JFaceResources.getColorRegistry().get(self.HEADER_FG_COLOR))
        l.setLayoutData(GridData(GridData.FILL_BOTH))

        iconComp = Composite(topArea,SWT.NONE)
        iconComp.setLayoutData(GridData())
        iconComp.setLayout(GridLayout(2,False))
        iconComp.setBackground(JFaceResources.getColorRegistry().get(self.HEADER_BG_COLOR))

        gl = GridLayout(2,False)
        gl.marginBottom=0
        gl.marginTop=0
        gl.marginHeight=0
        gl.marginWidth=0
        gl.marginLeft=0
        gl.marginRight=0
        iconComp.setLayout(gl)
        
        helpIcon = Label(iconComp,SWT.NONE)
        helpIcon.setBackground(JFaceResources.getColorRegistry().get(self.HEADER_BG_COLOR))
        helpIcon.setImage(JFaceResources.getImage(self.HEADER_HELP_ICON))
        
        closeIcon = Label(iconComp,SWT.NONE)
        closeIcon.setBackground(JFaceResources.getColorRegistry().get(self.HEADER_BG_COLOR))
        closeIcon.setImage(JFaceResources.getImage(self.HEADER_CLOSE_ICON))
        
        self.createContentArea(comp, event).setLayoutData(GridData(GridData.FILL_BOTH))
        return comp		

    def isHideOnMouseDown(self):
        return False
		
    @classmethod
    def enableFor(cls, viewer, style):
        FancyToolTipSupport(viewer, style, False)

	
display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

v = TableViewer(shell, SWT.FULL_SELECTION)
v.getTable().setLinesVisible(True)
v.getTable().setHeaderVisible(True)
v.setContentProvider(MyContentProvider())
FancyToolTipSupport.enableFor(v,ToolTip.NO_RECREATE)

class MyCellLabelProvider(CellLabelProvider):
    def getToolTipText(self, element):
        return "Custom tooltip for " + element + " - you can: \n- pop up any control you want\n- define delays\n - ... \nGo and get Eclipse M4 from <a>http:#www.eclipse.org</a>"
	
    def getToolTipShift(self, *args):
        return Point(5, 5)
	
    def getToolTipDisplayDelayTime(self, *args):
        return 100
	
    def getToolTipTimeDisplayed(self, *args):
        return 5000
	
    def update(self, cell):
        cell.setText(cell.getElement())

labelProvider = MyCellLabelProvider()

column = TableViewerColumn(v, SWT.NONE)
column.setLabelProvider(labelProvider)
column.getColumn().setText("Column 1")
column.getColumn().setWidth(100)

v.setInput("")

shell.setSize(200, 200)
shell.setText("Custom Tooltips")
shell.open()

while (not shell.isDisposed()):
	if (not display.readAndDispatch()):
		display.sleep()
	


display.dispose()
	



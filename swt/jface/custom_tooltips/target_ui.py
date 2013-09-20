##******************************************************************************
## Copyright (c) 2006, 2010 Tom Schindl and others.
## All rights reserved. This program and the accompanying materials
## are made available under the terms of the Eclipse Public License v1.0
## which accompanies this distribution, and is available at
## http://www.eclipse.org/legal/epl-v10.html
##
## Contributors:
##     Tom Schindl - initial API and implementation
## ******************************************************************************


from org.eclipse.jface.resource import ImageDescriptor
from org.eclipse.jface.resource import JFaceResources
from org.eclipse.jface.util import Policy
from org.eclipse.jface.window import DefaultToolTip
from org.eclipse.jface.window import ToolTip
from org.eclipse.swt import SWT
from org.eclipse.swt.events import MouseAdapter
from org.eclipse.swt.events import MouseEvent
from org.eclipse.swt.events import SelectionAdapter
from org.eclipse.swt.events import SelectionEvent
from org.eclipse.swt.graphics import Point
from org.eclipse.swt.graphics import RGB
from org.eclipse.swt.layout import FillLayout
from org.eclipse.swt.layout import GridData
from org.eclipse.swt.layout import GridLayout
from org.eclipse.swt.layout import RowLayout
from org.eclipse.swt.widgets import Button
from org.eclipse.swt.widgets import Composite
from org.eclipse.swt.widgets import Control
from org.eclipse.swt.widgets import Display
from org.eclipse.swt.widgets import Event
from org.eclipse.swt.widgets import Label
from org.eclipse.swt.widgets import Link
from org.eclipse.swt.widgets import MessageBox
from org.eclipse.swt.widgets import Shell
from org.eclipse.swt.widgets import Text
import os

##*
## Demonstrate usage of custom toolstips for controls
## 
## @author Tom Schindl
## 
## 

class MyToolTip(ToolTip):
    headerText = "ToolTip-Header"

    HEADER_BG_COLOR = Policy.JFACE + ".TOOLTIP_HEAD_BG_COLOR"
    HEADER_FG_COLOR = Policy.JFACE + ".TOOLTIP_HEAD_FG_COLOR"
    HEADER_FONT = Policy.JFACE + ".TOOLTIP_HEAD_FONT"
    HEADER_CLOSE_ICON = Policy.JFACE + ".TOOLTIP_CLOSE_ICON"
    HEADER_HELP_ICON = Policy.JFACE + ".TOOLTIP_HELP_ICON"

    def __init__(self, control):
        ToolTip.__init__(self, control)        
        self.parentShell = control.getShell()

    def createContentArea(self, parent):
        comp = Composite(parent,SWT.NONE)
        comp.setBackground(parent.getDisplay().getSystemColor(SWT.COLOR_INFO_BACKGROUND))
        layout = FillLayout()
        layout.marginWidth=5
        comp.setLayout(layout)
        l = Link(comp,SWT.NONE)
        l.setText("This a custom tooltip you can: \n- pop up any control you want\n- define delays\n - ... \nGo and get Eclipse M4 from <a>http:#www.eclipse.org</a>")
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
        
        self.createContentArea(comp).setLayoutData(GridData(GridData.FILL_BOTH))
        return comp
		
def setup(parent):
    JFaceResources.getColorRegistry().put(MyToolTip.HEADER_BG_COLOR, RGB(255,255,255))
    JFaceResources.getFontRegistry().put(MyToolTip.HEADER_FONT, JFaceResources.getFontRegistry().getBold(JFaceResources.getDefaultFont().getFontData()[0].getName()).getFontData())


    JFaceResources.getImageRegistry().put(MyToolTip.HEADER_CLOSE_ICON, ImageDescriptor.createFromFile(None, os.path.abspath("showerr_tsk.gif")))
    JFaceResources.getImageRegistry().put(MyToolTip.HEADER_HELP_ICON, ImageDescriptor.createFromFile(None, os.path.abspath("linkto_help.gif")))
    
    l1 = Label(parent, SWT.NONE)
    l1.setText("First")

    text = Text(parent,SWT.BORDER)
    text.setText("Hello World")

    myTooltipLabel = MyToolTip(text)

    myTooltipLabel.setShift(Point(-5, -5))
    myTooltipLabel.setHideOnMouseDown(False)
    myTooltipLabel.activate()
    l2 = Label(parent, SWT.NONE)
    l2.setText("Second")

    text = Text(parent,SWT.BORDER)
    text.setText("Hello World")
    toolTip = DefaultToolTip(text)
    toolTip.setText("Hello World\nHello World")
    toolTip.setBackgroundColor(parent.getDisplay().getSystemColor(SWT.COLOR_RED))

    b = Button(parent,SWT.PUSH)
    b.setText("Popup on press")

    toolTipDelayed = DefaultToolTip(b,ToolTip.RECREATE,True)
    toolTipDelayed.setText("Hello World\nHello World")
    toolTipDelayed.setBackgroundColor(parent.getDisplay().getSystemColor(SWT.COLOR_RED))
    toolTipDelayed.setHideDelay(2000)
				
	
if __name__ == "__main__":
    display = Display()

    shell = Shell(display)
    shell.setLayout(RowLayout())
    shell.setText("Custom Tooltips")
    setup(shell)

    shell.open()

    while not shell.isDisposed():
        if not display.readAndDispatch():
            display.sleep()
		
    display.dispose()
	


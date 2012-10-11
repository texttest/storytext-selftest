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
from org.eclipse.jface.fieldassist import ControlDecoration

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

bar = Menu(shell, SWT.BAR)
shell.setMenuBar(bar)
fileItem = MenuItem(bar, SWT.CASCADE)
fileItem.setText("&File")
submenu = Menu(shell, SWT.DROP_DOWN)
fileItem.setMenu(submenu)
item = MenuItem(submenu, SWT.PUSH)
item.setText("Describe")

composite = Composite(shell, SWT.NONE)
layout = GridLayout(2, False)
composite.setLayout(layout)

label = Label(composite, SWT.NONE)
label.setText("Name")
text = Text(composite, SWT.NONE)
text.setToolTipText("Your Full Name Please!")

from org.eclipse.jface.fieldassist import FieldDecorationRegistry

decoUseless = ControlDecoration(text, SWT.TOP | SWT.RIGHT)
decoUseless.hide()

deco = ControlDecoration(text, SWT.TOP | SWT.LEFT)
image = FieldDecorationRegistry.getDefault().getFieldDecoration(FieldDecorationRegistry.DEC_ERROR).getImage();
deco.setDescriptionText("Name may not be empty")
deco.setImage(image)


label2 = Label(composite, SWT.NONE)
label2.setText("City")
text2 = Text(composite, SWT.NONE)

deco2 = ControlDecoration(text2, SWT.TOP | SWT.RIGHT)
image = FieldDecorationRegistry.getDefault().getFieldDecoration(FieldDecorationRegistry.DEC_INFORMATION).getImage();
deco2.setImage(image)
deco2.hide()

class PrintListener(Listener):
    def handleEvent(self, e):
        print "You are", text.getText(), "and you live in", text2.getText()
        
item.addListener(SWT.Selection, PrintListener())

class NameListener(Listener):
    def handleEvent(self, e):
        if e.widget.getText():
            deco.hide()
        else:
            deco.show()

text.addListener(SWT.Modify, NameListener())

class CityListener(Listener):
    def handleEvent(self, e):
        if e.widget.getText() == "London":
            deco2.show()
            deco2.setDescriptionText("London is in England!")
        else:
            deco2.hide()

text2.addListener(SWT.Modify, CityListener())

shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

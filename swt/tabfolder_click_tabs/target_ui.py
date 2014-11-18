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
from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell, Menu, MenuItem, TabFolder, TabItem, Text, Listener, Event
from org.eclipse.swt.layout import FillLayout
from org.eclipse.swt.graphics import Image,GC
from java.lang import Runnable

def makeImage(display, size):
    image = Image(display, size, size)
    color = display.getSystemColor(SWT.COLOR_RED)
    gc = GC(image)
    gc.setBackground(color)
    gc.fillRectangle(image.getBounds())
    gc.dispose()
    return image

display = Display()
shell = Shell(display)
shell.setLayout(FillLayout())

bar = Menu(shell, SWT.BAR)
shell.setMenuBar(bar)
fileItem = MenuItem(bar, SWT.CASCADE)
fileItem.setText("&File")
submenu = Menu(shell, SWT.DROP_DOWN)
fileItem.setMenu(submenu)
menuItem = MenuItem(submenu, SWT.PUSH)
menuItem.setText("Rename")

folder = TabFolder(shell, SWT.BORDER)
for i in range(2):
    item = TabItem(folder, SWT.CLOSE)
    item.setText("Item " + str(i))
    text = Text(folder, SWT.MULTI)
    text.setText("Content for Item " + str(i))
    text.setEnabled(False)
    item.setImage(makeImage(display, (i + 1) * 8))
    item.setControl(text)

class TabSelectRunnable(Runnable):
    def run(self):
        if not folder.isDisposed():
            self.generateSelectionEvent()
        x = Event()
        x.text = "tab to be selected"
        folder.notifyListeners(1234, x)

    def generateSelectionEvent(self):
        folder.setSelection(0)
        event = Event()
        event.widget = folder
        event.item = folder.getItem(0)
        event.type = SWT.Selection
        event.display = display
        folder.notifyListeners(SWT.Selection, event)

	
class RenameListener(Listener):
    def handleEvent(self, e):
        for item in folder.getSelection():
            item.getControl().setEnabled(True)
            item.setText("New")
        display.timerExec(1000, TabSelectRunnable())

class DisposeListener(Listener):
    def handleEvent(self, e):
        if isinstance(e.widget, TabItem):
            e.widget.getImage().dispose()
        
menuItem.addListener(SWT.Selection, RenameListener())
display.addFilter(SWT.Dispose, DisposeListener())

shell.pack()
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

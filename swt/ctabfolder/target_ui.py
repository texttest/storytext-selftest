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
from org.eclipse.swt.widgets import Shell, Display, Menu, MenuItem, Text, Listener
from org.eclipse.swt.layout import FillLayout
from org.eclipse.swt.custom import CTabFolder, CTabItem
from org.eclipse.swt.graphics import Image, GC

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

class ActivateListener(Listener):
    def handleEvent(self, e):
        print e.widget.getSelection().getText() + " has been activated"

folder = CTabFolder(shell, SWT.BORDER)
folder.setData("org.eclipse.swtbot.widget.key", "The Folder");
folder.addListener(SWT.Activate, ActivateListener())
for i in range(2):
    item = CTabItem(folder, SWT.CLOSE)
    item.setText("Item " + str(i))
    text = Text(folder, SWT.MULTI)
    text.setText("Content for Item " + str(i))
    text.setEnabled(False)
    item.setImage(makeImage(display, (i + 1) * 8))
    item.setControl(text)
    item.addListener(SWT.Activate, ActivateListener())
	
class RenameListener(Listener):
    def handleEvent(self, e):
        folder.getSelection().getControl().setEnabled(True)
        folder.getSelection().setText("New")

class DisposeListener(Listener):
    def handleEvent(self, e):
        if isinstance(e.widget, CTabItem):
            e.widget.getImage().dispose()
        
menuItem.addListener(SWT.Selection, RenameListener())
display.addFilter(SWT.Dispose, DisposeListener())

shell.pack()
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

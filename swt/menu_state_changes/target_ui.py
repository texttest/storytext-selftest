
""" Copyright (c) 2000, 2004 IBM Corporation and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *
 * Contributors:
 *     IBM Corporation - initial API and implementation

 * Menu example snippet: create a bar and pull down menu (accelerators, mnemonics)
 *
 * For a list of all SWT example snippets see
 * http://www.eclipse.org/swt/snippets/ """

from org.eclipse.swt import *
from org.eclipse.swt.widgets import *

display = Display()
shell = Shell(display)

class MyShellListener(Listener):
    def handleEvent(self, e):
        print "Closed!"

bar = Menu(shell, SWT.BAR)
shell.setMenuBar(bar)
shell.addListener(SWT.Close, MyShellListener())
fileItem = MenuItem(bar, SWT.CASCADE)
fileItem.setText("&File")
submenu = Menu(shell, SWT.DROP_DOWN)
fileItem.setMenu(submenu)

class ToggleListener(Listener):
    def handleEvent(self, e):
        e.widget.setEnabled(not e.widget.isEnabled())

def fillSubmenu(submenu, start, end):
    for i in range(start, end):
        item = MenuItem(submenu, SWT.PUSH)
        item.addListener(SWT.Selection, ToggleListener())
        item.setText("Item " + str(i))

class ExitListener(Listener):
    def handleEvent(self, e):
        shell.close()

fillSubmenu(submenu, 1, 5)
smItem = MenuItem(submenu, SWT.CASCADE)
smItem.setText("Submenu..")
menu = Menu(shell, SWT.DROP_DOWN)
smItem.setMenu(menu)
fillSubmenu(menu, 5, 7)
exititem = MenuItem(submenu, SWT.PUSH)
exititem.setText("E&xit")
exititem.addListener(SWT.Selection, ExitListener())

shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

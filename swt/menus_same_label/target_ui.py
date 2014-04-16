
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

from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell, Listener, Menu, MenuItem

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
item = MenuItem(submenu, SWT.PUSH)

class PrintListener(Listener):
    def handleEvent(self, e):
        print "Normal Item"

class SubPrintListener(Listener):
    def handleEvent(self, e):
        print "Submenu Item"

item.addListener(SWT.Selection, PrintListener())
item.setText("Item")

item2 = MenuItem(submenu, SWT.CASCADE)
item2.setText("Submenu")

subsubmenu = Menu(shell, SWT.DROP_DOWN)
item2.setMenu(subsubmenu)
subitem = MenuItem(subsubmenu, SWT.PUSH)
subitem.setText("Item")
subitem.addListener(SWT.Selection, SubPrintListener())

class ExitListener(Listener):
    def handleEvent(self, e):
        shell.close()

exititem = MenuItem(submenu, SWT.PUSH)
exititem.setText("E&xit")
exititem.addListener(SWT.Selection, ExitListener())

shell.setSize(200, 200)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()
        
display.dispose()

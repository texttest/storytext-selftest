
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
item = MenuItem(submenu, SWT.RADIO)

class PrintListener(Listener):
    def handleEvent(self, e):
        item = e.widget;
        if item.getSelection():
            print item.getText() + " selected"
        else:
            print item.getText() + " unselected"

item.addListener(SWT.Selection, PrintListener())
item.setText("Black")
item2 = MenuItem(submenu, SWT.RADIO)
item2.setText("White")
item2.addListener(SWT.Selection, PrintListener())
item.setSelection(True)

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

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

import os
    
html = '''<head><style type="text/css">
body {background-color:#FFFFFF;font:12px arial,sans-serif} table {font:12px arial,sans-serif}</style>
</head><body><table cellspacing="0" cellpadding="1" border="0" align="left"><tbody>
<tr><td>Table-0</td></tr>
<tr><td><table cellspacing="0" cellpadding="1" border="0" align="left"><tbody>
<tr><td>Table-1</TD></tr>
<tr><td><table cellspacing="0" cellpadding="1" border="0" align="left"><tbody>
<tr><td><table></table>Table-2</td></tr>
<tr><td>Non-breaking spaces:</td><td width=30>Hello &nbsp; world</td></tr>
</tbody></table></td>
</tr></tbody></table></td></tr>
</tbody></table></body>'''

from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.layout import *
from org.eclipse.swt.browser import *

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
item.setText("Select &All\tCtrl+A")

browser = Browser(shell, SWT.None)
browser.setUrl("about:config");

class BrowserListener(Listener):
    def handleEvent(self, e):
        browser.setText(html)

item.addListener(SWT.Selection, BrowserListener())

shell.pack()
shell.setSize(500, 500)
shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()

display.dispose()

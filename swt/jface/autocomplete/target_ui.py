
from org.eclipse.jface.bindings.keys import KeyStroke
from org.eclipse.jface.bindings.keys import ParseException
from org.eclipse.jface.fieldassist import ContentProposal
from org.eclipse.jface.fieldassist import ContentProposalAdapter
from org.eclipse.jface.fieldassist import SimpleContentProposalProvider
from org.eclipse.jface.fieldassist import TextContentAdapter
from org.eclipse.jface.viewers import ILabelProvider
from org.eclipse.jface.viewers import ILabelProviderListener
from org.eclipse.swt import SWT
from org.eclipse.swt.graphics import Image
from org.eclipse.swt.layout import GridLayout
from org.eclipse.swt.widgets import Display
from org.eclipse.swt.widgets import Shell
from org.eclipse.swt.widgets import Text

display = Display()
shell = Shell(display)
shell.setLayout(GridLayout(1, False))
shell.setText("Autocomplete")

text = Text(shell, SWT.BORDER)

proposals = [ "abc", "bcd", "cde", "abc2", "bcd2", "cde2" ]
autoActivationCharacters = ""
simpleContentProposalProvider = SimpleContentProposalProvider(proposals)

for prop in proposals:
    c = prop[0]
    if autoActivationCharacters.find(c) == -1:
       autoActivationCharacters += c

keyStroke = None
simpleContentProposalProvider.setFiltering(True)
try:
    keyStroke = KeyStroke.getInstance("Ctrl+Space")
except ParseException:
    print "KeyStroke Parse Exception"

proposalAdapter = ContentProposalAdapter(text, TextContentAdapter(),
                                         simpleContentProposalProvider, keyStroke, autoActivationCharacters)

proposalAdapter.setProposalAcceptanceStyle(ContentProposalAdapter.PROPOSAL_REPLACE)


class MyLabelProvider(ILabelProvider):
    def removeListener(self, listener):
        pass

    def isLabelProperty(self, element, prop):
        return False

    def dispose(self):
        pass

    def addListener(self, listener):
        pass

    def getText(self, element):
        return element.getLabel()

    def getImage(self, element):
        pass


proposalAdapter.setLabelProvider(MyLabelProvider())

shell.open()
while not shell.isDisposed():
    if not display.readAndDispatch():
        display.sleep()


display.dispose()
   

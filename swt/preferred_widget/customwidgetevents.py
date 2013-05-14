
from storytext.javaswttoolkit import simulator as swtsimulator
import org.eclipse.swtbot.swt.finder as swtbot

class ButtonSelectEvent(swtsimulator.SelectEvent):
    def isPreferred(self):
        return swtsimulator.runOnUIThread(self.widget.widget.widget.getImage) is not None

# Standard name for module containing custom widget events
customEventTypes = [ (swtbot.widgets.SWTBotButton, [ ButtonSelectEvent ])]


from storytext.javaswttoolkit import simulator as swtsimulator
import org.eclipse.swtbot.swt.finder as swtbot

class ButtonSelectEvent(swtsimulator.SelectEvent):
    def _generate(self, *args):
        # Just to make sure we can plug in this mechanism...
        print "We faked a button click!"
        self.widget.click()

# Standard name for module containing custom widget events
customEventTypes = [ (swtbot.widgets.SWTBotButton, [ ButtonSelectEvent ])]

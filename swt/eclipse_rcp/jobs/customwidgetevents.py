
from storytext.javaswttoolkit import simulator as swtsimulator
from storytext.javarcptoolkit import jobsynchroniser
import org.eclipse.swtbot.swt.finder as swtbot
# Test we can request this
jobsynchroniser.JobListener.systemJobNames.append("close dialog")

class ButtonSelectEvent(swtsimulator.SelectEvent):
    def _generate(self, *args):
        # Just to make sure we can plug in this mechanism...
        print "We faked a button click!"
        self.widget.click()

# Standard name for module containing custom widget events
customEventTypes = [ (swtbot.widgets.SWTBotButton, [ ButtonSelectEvent ])]


from gtkusecase.simulator.baseevents import SignalEvent
import gtk

class MyButtonEvent(SignalEvent):
    def generate(self, *args):
        print "We faked a button click!"
        SignalEvent.generate(self, *args)

    def shouldRecord(self, *args):
        print "Refusing to record the button click!"
        return False

class InsertEvent(SignalEvent):
    signalName = "row-inserted"
    def connectRecord(self, method):
        self._connectRecord(self.widget.get_model(), method)

# Standard name for module containing custom widget events
customEventTypes = [(gtk.Button, [ MyButtonEvent ]),
                    (gtk.TreeView, [ InsertEvent])]

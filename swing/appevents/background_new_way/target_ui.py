from javax import swing
from java.awt import BorderLayout, Toolkit, AWTEvent, Frame
from java.awt.event import ActionListener, ActionEvent, MouseEvent

class ApplicationEvent(MouseEvent):
    def __init__(self, component, message):
        MouseEvent.__init__(self, component, MouseEvent.MOUSE_PRESSED, 0, 0, 0, 0, 0, False)
        self.message = message

    def getApplicationEventMessage(self):
        return self.message

class ApplicationEventManager(swing.JComponent):
    instance = None
    
    def sendApplicationEvent(self, message):
        ev = ApplicationEvent(self, message)
        Toolkit.getDefaultToolkit().getSystemEventQueue().postEvent(ev)

ApplicationEventManager.instance = ApplicationEventManager()

class ApplicationEventApp:
    def make_ui(self):
        self.stupidFrame = swing.JFrame("Not Really")
        self.frame = swing.JFrame("Close Buttons")
        self.frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        self.frame.setSize(200, 200);
        button1 = swing.JButton("Why?", actionPerformed=self.handleButton)
        self.button2 = swing.JButton("Exit", actionPerformed=self.close)
        self.button2.setEnabled(False)

        panel = swing.JPanel()
        panel.add(button1)
        panel.add(self.button2)
        self.frame.add(panel)
        self.frame.pack()
        self.stupidFrame.setVisible(False)
        self.frame.setVisible(True)
    
    def close(self, event):
        self.stupidFrame.dispose()
        self.frame.dispose()
    
    def handleButton(self, event):
        class ButtonListener(ActionListener):
            def actionPerformed(lself, event):
                print "Because"
                self.button2.setEnabled(True)
                ApplicationEventManager.instance.sendApplicationEvent("Exit button to be enabled")
                
        timer = swing.Timer(1000, ButtonListener())
        timer.setRepeats(False)
        timer.start()

    @staticmethod
    def main():
        app = ApplicationEventApp()
        app.make_ui()

ApplicationEventApp.main()


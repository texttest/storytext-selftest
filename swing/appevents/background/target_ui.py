from javax import swing
from java.awt import BorderLayout, Toolkit, AWTEvent
from java.awt.event import ActionListener, ActionEvent

class ApplicationEeventApp:
    def make_ui(self):
        self.frame = swing.JFrame("Close Buttons")
        self.frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        self.frame.setSize(200, 200);
        button1 = swing.JButton("Why?", actionPerformed=self.handleButton)
        self.button2 = swing.JButton("Exit", actionPerformed=self.close)
        self.button2.setEnabled(False)
        self.button3 = swing.JButton("ApplicationEvent Exit button to be enabled")
        self.button3.setVisible(False)

        panel = swing.JPanel()
        panel.add(button1)
        panel.add(self.button2)
        panel.add(self.button3)
        self.frame.add(panel)
        self.frame.pack()
        self.frame.setVisible(True)
    
    def close(self, event):
        self.frame.dispose()
    
        
    def handleButton(self, event):
        class ButtonListener(ActionListener):
            def actionPerformed(lself, event):
                print "Because"
                self.button2.setEnabled(True)
                self.button3.doClick()
                #eventQueue = Toolkit.getDefaultToolkit().getSystemEventQueue()
                #eventQueue.postEvent(ActionEvent(self.button2, AWTEvent.RESERVED_ID_MAX + 1234, "Text to be displayed"))
        timer = swing.Timer(1000, ButtonListener())
        timer.setRepeats(False)
        timer.start()

    @staticmethod
    def main():
        app = ApplicationEeventApp()
        app.make_ui()

ApplicationEeventApp.main()


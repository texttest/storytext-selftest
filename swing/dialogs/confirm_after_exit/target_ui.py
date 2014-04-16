from javax.swing import JFrame, JPanel, JButton, JOptionPane
from java.awt import BorderLayout
from java.awt.event import WindowAdapter

class ConfirmDialogApp:                  
    def make_ui(self):
        class MyWindowListener(WindowAdapter):
            def windowClosing(listenerSelf, event):
                confirmed = JOptionPane.showConfirmDialog(self.frame, 
                                                    "Are you sure you want to exit?", 
                                                    "User Confirmation", 
                                                    JOptionPane.YES_NO_OPTION)
                if confirmed == JOptionPane.YES_OPTION:
                    self.frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
                    print "Yes option clicked"
                    self.frame.dispose()
                elif confirmed == JOptionPane.NO_OPTION:
                    self.frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE)
                    print "No option clicked", confirmed
                else:
                    print "Other action has occurred", confirmed

        self.frame = JFrame("Confirm Dialog Demo")
        self.frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        self.frame.addWindowListener(MyWindowListener())
        panel = JPanel()
        panel.add(JButton("Do nothing"))
        self.frame.add(panel)
        self.frame.pack()
        self.frame.setSize(300, 300)
        self.frame.setVisible(True)

    @staticmethod                    
    def main():
        app = ConfirmDialogApp()
        app.make_ui()

ConfirmDialogApp.main()

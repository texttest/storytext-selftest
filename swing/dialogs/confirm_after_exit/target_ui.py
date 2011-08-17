from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent, WindowAdapter
from java.lang import System, Runnable, Thread
from javax.swing import JOptionPane, SwingUtilities

class ConfirmDialogApp:                  
    def make_ui(self):
        class MyWindowListener(WindowAdapter):
            def windowClosing(listenerSelf, event):
                confirmed = JOptionPane.showConfirmDialog(self.frame, 
                                                    "Are you sure you want to exit?", 
                                                    "User Confirmation", 
                                                    JOptionPane.YES_NO_OPTION)
                if confirmed == JOptionPane.YES_OPTION:
                    self.frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
                    print "Yes option clicked"
                    self.frame.dispose()
                else:
                    self.frame.setDefaultCloseOperation(swing.JFrame.DO_NOTHING_ON_CLOSE)
                    print "No option clicked", confirmed

        self.frame = swing.JFrame("Confirm Dialog Demo")
        self.frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        self.frame.setLayout(BorderLayout())
        self.frame.addWindowListener(MyWindowListener())
        panel = swing.JPanel()
        panel.add(swing.JButton("Do nothing"))
        self.frame.add(panel)
        self.frame.pack()
        self.frame.setVisible(True)

    @staticmethod                    
    def main():
        app = ConfirmDialogApp()
        app.make_ui()

ConfirmDialogApp.main()

from javax import swing
from java.awt import BorderLayout

class CheckBoxApp:
        
    def make_ui(self):
        frame = swing.JFrame("Check box demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        cBox1 = swing.JCheckBox("First", actionPerformed=self.printButton)
        cBox2 = swing.JCheckBox("Second", actionPerformed=self.printButton)
        newContentPane = swing.JPanel()
        newContentPane.add(cBox1)
        newContentPane.add(cBox2)
        frame.add(newContentPane)
        frame.pack()
        frame.setVisible(True)

    def printButton(self, event):
        widget = event.getSource()
        if widget.isSelected():
            print "Selected the", widget.getText(), "check box"
        else:
            print "Deselected the", widget.getText(), "check box"

    @staticmethod            
    def main():
        app = CheckBoxApp()
        app.make_ui()

CheckBoxApp.main()


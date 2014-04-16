from javax.swing import JFrame, JPanel, JCheckBox
from java.awt import BorderLayout

class CheckBoxApp:
        
    def make_ui(self):
        frame = JFrame("Check box demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        cBox1 = JCheckBox("First", actionPerformed=self.printButton)
        cBox2 = JCheckBox("Second", actionPerformed=self.printButton)
        newContentPane = JPanel()
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


from java.awt import BorderLayout
from javax.swing import JRadioButton, JPanel, JFrame, ButtonGroup

class RadioButtonApp:
        
    def make_ui(self):
        frame = JFrame("Radio button demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        rButton1 = JRadioButton("First", actionPerformed=self.printButton)
        rButton2 = JRadioButton("Second", actionPerformed=self.printButton)
        newContentPane = JPanel()
        newContentPane.add(rButton1)
        newContentPane.add(rButton2)
        buttonGroup = ButtonGroup()
        buttonGroup.add(rButton1)
        buttonGroup.add(rButton2)
        frame.add(newContentPane)
        frame.pack()
        frame.setVisible(True)

    def printButton(self, event):
        widget = event.getSource()
        if widget.isSelected():
            print "Selected the", widget.getText(), "button"

    @staticmethod
    def main():
        app = RadioButtonApp()
        app.make_ui()

RadioButtonApp.main()


from javax import swing
from java.awt import BorderLayout

class RadioButtonApp:
        
    def make_ui(self):
        frame = swing.JFrame("Radio button demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        rButton1 = swing.JRadioButton("First", actionPerformed=self.printButton)
        rButton2 = swing.JRadioButton("Second", actionPerformed=self.printButton)
        newContentPane = swing.JPanel()
        newContentPane.add(rButton1)
        newContentPane.add(rButton2)
        buttonGroup = swing.ButtonGroup()
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


from javax import swing
from java.awt import BorderLayout

class ToggleButtonApp:
        
    def make_ui(self):
        frame = swing.JFrame("Toggle Button demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        cBox1 = swing.JToggleButton("First", actionPerformed=self.printButton)
        cBox2 = swing.JToggleButton("Second", actionPerformed=self.printButton)
        newContentPane = swing.JPanel()
        newContentPane.add(cBox1)
        newContentPane.add(cBox2)
        frame.add(newContentPane)
        frame.pack()
        frame.setVisible(True)

    def printButton(self, event):
        widget = event.getSource()
        if widget.isSelected():
            print "Selected the", widget.getText(), "toggle button"
        else:
            print "Deselected the", widget.getText(), "toggle button"

    @staticmethod            
    def main():
        app = ToggleButtonApp()
        app.make_ui()

ToggleButtonApp.main()


from javax import swing
from java.awt import BorderLayout
from java.awt.event import ActionListener

class TextFieldApp: 
    def make_ui(self):
        frame = swing.JFrame("Text field demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setSize(300, 200)
        button = swing.JButton("Do nothing")
        panel2 = swing.JPanel(BorderLayout())
        textLabel = swing.JLabel("Text: ")
        textField = swing.JTextField()
        panel2.add(textLabel, BorderLayout.WEST)
        panel2.add(textField, BorderLayout.CENTER)
        panel = swing.JPanel(BorderLayout())
        panel.add(button)
        panel3 = swing.JPanel()
        frame.getContentPane().add(panel, BorderLayout.NORTH)
        frame.getContentPane().add(panel2, BorderLayout.CENTER)
        frame.getContentPane().add(panel3, BorderLayout.SOUTH)
        #frame.pack()
        frame.setVisible(True)

    @staticmethod        
    def main():
        app = TextFieldApp()
        app.make_ui()

TextFieldApp.main()

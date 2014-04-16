from java.awt import BorderLayout
from javax.swing import JFrame, JLabel, JPanel, JButton, JTextField, JSeparator

class MyTextFieldSubClass(JTextField):
    pass

class TextFieldApp: 
    def make_ui(self):
        frame = JFrame("Text field demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setSize(300, 200)
        button = JButton("Do nothing")
        panel2 = JPanel(BorderLayout())
        textLabel = JLabel("Some Text: ")
        textField = MyTextFieldSubClass()
        panel2.add(textLabel, BorderLayout.WEST)
        panel2.add(textField, BorderLayout.CENTER)
        panel = JPanel(BorderLayout())
        panel.add(button)
        frame.getContentPane().add(panel, BorderLayout.NORTH)
        frame.getContentPane().add(JSeparator(), BorderLayout.CENTER)
        frame.getContentPane().add(panel2, BorderLayout.SOUTH)
        #frame.pack()
        frame.setVisible(True)

    @staticmethod        
    def main():
        app = TextFieldApp()
        app.make_ui()

TextFieldApp.main()

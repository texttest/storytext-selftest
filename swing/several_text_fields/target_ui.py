from java.awt import BorderLayout
from javax.swing import JButton, JPanel, JFrame, JLabel, JTextField, JPasswordField

class MyTextFieldSubClass(JTextField):
    pass

class TextFieldApp: 
    def make_ui(self):
        frame = JFrame("Text field demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setSize(300, 200)
        button = JButton("Do nothing")
        panel = JPanel(BorderLayout())
        panel.add(button)
        frame.getContentPane().add(panel, BorderLayout.NORTH)
        frame.getContentPane().add(self.makeTextFieldPanel("User Name: ", MyTextFieldSubClass), BorderLayout.CENTER)
        frame.getContentPane().add(self.makeTextFieldPanel("Password: ", JPasswordField), BorderLayout.SOUTH)
        #frame.pack()
        frame.setVisible(True)

    def makeTextFieldPanel(self, label, fieldClass):
        panel = JPanel(BorderLayout())
        textLabel = JLabel(label)
        textField = fieldClass()
        panel.add(textLabel, BorderLayout.WEST)
        panel.add(textField, BorderLayout.CENTER)
        return panel

    @staticmethod        
    def main():
        app = TextFieldApp()
        app.make_ui()

TextFieldApp.main()

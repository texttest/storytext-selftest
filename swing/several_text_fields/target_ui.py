from javax import swing
from java.awt import BorderLayout
from java.awt.event import ActionListener

class MyTextFieldSubClass(swing.JTextField):
    pass

class TextFieldApp: 
    def make_ui(self):
        frame = swing.JFrame("Text field demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setSize(300, 200)
        button = swing.JButton("Do nothing")
        panel = swing.JPanel(BorderLayout())
        panel.add(button)
        frame.getContentPane().add(panel, BorderLayout.NORTH)
        frame.getContentPane().add(self.makeTextFieldPanel("User Name: ", MyTextFieldSubClass), BorderLayout.CENTER)
        frame.getContentPane().add(self.makeTextFieldPanel("Password: ", swing.JPasswordField), BorderLayout.SOUTH)
        #frame.pack()
        frame.setVisible(True)

    def makeTextFieldPanel(self, label, fieldClass):
        panel = swing.JPanel(BorderLayout())
        textLabel = swing.JLabel(label)
        textField = fieldClass()
        panel.add(textLabel, BorderLayout.WEST)
        panel.add(textField, BorderLayout.CENTER)
        return panel

    @staticmethod        
    def main():
        app = TextFieldApp()
        app.make_ui()

TextFieldApp.main()

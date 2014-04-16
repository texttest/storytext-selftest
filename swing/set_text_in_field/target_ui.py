from java.awt import BorderLayout
from javax.swing import JButton, JPanel, JFrame, JLabel, JTextField

class TextFieldApp: 
    def make_ui(self):
        frame = JFrame("Text field demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setSize(300, 200)
        button = JButton("Change text", actionPerformed=self.changeText)
        panel2 = JPanel(BorderLayout())
        textLabel = JLabel("Some Text: ")
        self.textField = JTextField()
        panel2.add(textLabel, BorderLayout.WEST)
        panel2.add(self.textField, BorderLayout.CENTER)
        panel = JPanel(BorderLayout())
        panel.add(button)
        panel3 = JPanel()
        frame.getContentPane().add(panel, BorderLayout.NORTH)
        frame.getContentPane().add(panel2, BorderLayout.CENTER)
        frame.getContentPane().add(panel3, BorderLayout.SOUTH)
        #frame.pack()
        frame.setVisible(True)

    def changeText(self, event):
        self.textField.setText("Changed!")

    @staticmethod        
    def main():
        app = TextFieldApp()
        app.make_ui()

TextFieldApp.main()

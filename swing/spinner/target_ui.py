from java.awt import BorderLayout
from javax.swing import JFrame, JLabel, JSpinner, JPanel, JButton, JSeparator, SpinnerNumberModel

class TextFieldApp: 
    def make_ui(self):
        frame = JFrame("Text field demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setSize(300, 200)
        button = JButton("Do nothing")
        panel2 = JPanel(BorderLayout())
        textLabel = JLabel("The Year: ")

        currentYear = 2011
        yearModel = SpinnerNumberModel(currentYear, #initial value
                                             currentYear - 100, #min
                                             currentYear + 100, #max
                                             1)                #step
        spinner = JSpinner(yearModel)
        textLabel.setLabelFor(spinner)
        #Make the year be formatted without a thousands separator.
        spinner.setEditor(JSpinner.NumberEditor(spinner, "#"));

        panel2.add(textLabel, BorderLayout.WEST)
        panel2.add(spinner, BorderLayout.CENTER)
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

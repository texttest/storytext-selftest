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
        textLabel = swing.JLabel("The Year: ")

        currentYear = 2011
        yearModel = swing.SpinnerNumberModel(currentYear, #initial value
                                             currentYear - 100, #min
                                             currentYear + 100, #max
                                             1)                #step
        spinner = swing.JSpinner(yearModel)
        textLabel.setLabelFor(spinner)
        #Make the year be formatted without a thousands separator.
        spinner.setEditor(swing.JSpinner.NumberEditor(spinner, "#"));

        panel2.add(textLabel, BorderLayout.WEST)
        panel2.add(spinner, BorderLayout.CENTER)
        panel = swing.JPanel(BorderLayout())
        panel.add(button)
        frame.getContentPane().add(panel, BorderLayout.NORTH)
        frame.getContentPane().add(swing.JSeparator(), BorderLayout.CENTER)
        frame.getContentPane().add(panel2, BorderLayout.SOUTH)


        #frame.pack()
        frame.setVisible(True)

    @staticmethod        
    def main():
        app = TextFieldApp()
        app.make_ui()

TextFieldApp.main()

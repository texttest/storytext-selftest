from javax.swing import JFrame, JPanel, JComboBox, WindowConstants
from java.awt import BorderLayout
from java.awt.event import ActionListener

class JComboBoxApp:
   
    def make_ui(self):
        class SelectionListener(ActionListener):
            def actionPerformed(listenerSelf, event):
                selected = self.cbox.selectedIndex
                if selected >= 0:
                    data = self.data[selected]
                    print data + " selected"
               
        frame = JFrame("Combo box demo")
        frame.setSize(200, 100)
        frame.setLayout(BorderLayout())

        self.data = ("One", "Two", "Three")
        self.cbox = JComboBox(self.data)
        self.cbox.setEditable(True)
        self.cbox.addActionListener(SelectionListener())
        panel = JPanel()
        panel.add(self.cbox)

        frame.add(panel, BorderLayout.CENTER)
        frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
        frame.setVisible(True)

    def main():
        app = JComboBoxApp()
        app.make_ui()
    main = staticmethod(main)

JComboBoxApp.main()

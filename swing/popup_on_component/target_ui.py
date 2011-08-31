from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import ActionListener, MouseAdapter
        
class PopupApp(ActionListener):        
    def make_ui(self):
        frame = swing.JFrame("Popup demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setSize(400, 200)
        editMenu = swing.JPopupMenu("Edit")
        editMenu.add(self.createMenuItem("Copy"))
        editMenu.add(self.createMenuItem("Paste"))
        newMenu = swing.JPopupMenu("New")
        newMenu.add(self.createMenuItem("Item 1"))
        newMenu.add(self.createMenuItem("Item 2"))

        newMenu2 = swing.JPopupMenu("New2")
        newMenu2.add(self.createMenuItem("Item 3"))
        newMenu2.add(self.createMenuItem("Item 4"))

        textLabel = swing.JLabel("Some Text")
        panel = swing.JPanel()
        panel.setComponentPopupMenu(newMenu)
        panel.setName("upper panel")

        panel2 = swing.JPanel()
        panel2.setLayout(BorderLayout())
        panel2.setComponentPopupMenu(newMenu2)
        panel2.setName("bottom panel")
        
        text = swing.JTextField()
        text.setComponentPopupMenu(editMenu)
        panel2.add(BorderLayout.WEST, textLabel)
        panel2.add(BorderLayout.SOUTH, text)
        frame.add(BorderLayout.NORTH, panel)
        frame.add(BorderLayout.SOUTH, panel2)
        frame.pack()
        frame.setVisible(True)
        
    def createMenuItem(self, name):
        item = swing.JMenuItem(name)
        item.addActionListener(self)
        return item
        
    def actionPerformed(self, event):
        print event.getActionCommand(), "performed"

    @staticmethod            
    def main():
        app = PopupApp()
        app.make_ui()

PopupApp.main()

from java.awt import BorderLayout
from java.awt.event import ActionListener
from javax.swing import JFrame, JPopupMenu, JLabel, JTextField, JPanel, JMenuItem
        
class PopupApp(ActionListener):        
    def make_ui(self):
        frame = JFrame("Popup demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setSize(400, 200)
        editMenu = JPopupMenu("Edit")
        editMenu.add(self.createMenuItem("Copy"))
        editMenu.add(self.createMenuItem("Paste"))
        newMenu = JPopupMenu("New")
        newMenu.add(self.createMenuItem("Item 1"))
        newMenu.add(self.createMenuItem("Item 2"))

        newMenu2 = JPopupMenu("New2")
        newMenu2.add(self.createMenuItem("Item 3"))
        newMenu2.add(self.createMenuItem("Item 4"))

        textLabel = JLabel("Some Text")
        panel = JPanel()
        panel.setComponentPopupMenu(newMenu)
        panel.setName("upper panel")

        panel2 = JPanel()
        panel2.setLayout(BorderLayout())
        panel2.setComponentPopupMenu(newMenu2)
        panel2.setName("bottom panel")
        
        text = JTextField()
        text.setComponentPopupMenu(editMenu)
        panel2.add(BorderLayout.WEST, textLabel)
        panel2.add(BorderLayout.SOUTH, text)
        frame.add(BorderLayout.NORTH, panel)
        frame.add(BorderLayout.SOUTH, panel2)
        frame.pack()
        frame.setVisible(True)
        
    def createMenuItem(self, name):
        item = JMenuItem(name)
        item.addActionListener(self)
        return item
        
    def actionPerformed(self, event):
        print event.getActionCommand(), "performed"

    @staticmethod            
    def main():
        app = PopupApp()
        app.make_ui()

PopupApp.main()

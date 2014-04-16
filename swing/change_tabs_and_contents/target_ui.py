from javax.swing import JFrame, JPanel, JButton, JTabbedPane, JLabel
from java.awt import BorderLayout, Dimension
from java.awt.event import ActionListener

class TabsApp:            
    def make_ui(self):
        self.labels = []
        frame = JFrame("Tabs demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setPreferredSize(Dimension(300, 250))
        panel = JPanel(BorderLayout())
        button = JButton("Enable!")
        class EnableListener(ActionListener):
            def actionPerformed(lself, *args):
                self.tabbedPane.setEnabledAt(0, True)
                self.labels[0].setVisible(True)
                
        button.addActionListener(EnableListener())
        panel.add(button, BorderLayout.NORTH)
        self.tabbedPane = self.createTabbedPane()
        panel.add(self.tabbedPane, BorderLayout.CENTER)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTabbedPane(self):                
        tPane = JTabbedPane(JTabbedPane.TOP)
        self.addTabs(tPane)
        return tPane
    
    def addTabs(self, tabbedPane):
        for i in range(1, 6):
            panel = JPanel()
            label = JLabel("content " + str(i))
            self.labels.append(label)
            panel.add(label)
            tabbedPane.add("Tab " + str(i), panel)
            label.setVisible(False)
            tabbedPane.setEnabledAt(i - 1, False)

    @staticmethod            
    def main():
        app = TabsApp()
        app.make_ui()

TabsApp.main()

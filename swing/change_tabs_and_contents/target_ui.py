from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent, ActionListener
from java.lang import System
class TabsApp:            
    def make_ui(self):
        self.labels = []
        frame = swing.JFrame("Tabs demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setPreferredSize(Dimension(300, 250))
        panel = swing.JPanel(BorderLayout())
        button = swing.JButton("Enable!")
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
        tPane = swing.JTabbedPane(swing.JTabbedPane.TOP)
        self.addTabs(tPane)
        return tPane
    
    def addTabs(self, tabbedPane):
        for i in range(1, 6):
            panel = swing.JPanel()
            label = swing.JLabel("content " + str(i))
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

from java.awt import BorderLayout, Dimension
from javax.swing import JFrame, JLabel, JPanel, JTabbedPane
from javax.swing.event import ChangeListener

class TabsApp:            
    def make_ui(self):
        frame = JFrame("Tabs demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setPreferredSize(Dimension(300, 250))
        frame.add(self.createTabbedPane())
        frame.pack()
        frame.setVisible(True)

    def createTabbedPane(self):
        class TabSelectionListener(ChangeListener):
            def stateChanged(listenerSelf, event):
                pane = event.getSource()
                index = pane.getSelectedIndex()
                # Shouldn't be visible, unless we're actually there
                pane.getComponentAt(0).getComponents()[0].setText("Edited")
                print pane.getTitleAt(index), "selected"
                
        tPane = JTabbedPane(JTabbedPane.TOP)
        self.addTabs(tPane)
        tPane.addChangeListener(TabSelectionListener())
        return tPane
    
    def addTabs(self, tabbedPane):
        for i in range(1, 6):
            panel = JPanel()
            panel.add(JLabel("content " + str(i)))
            tabbedPane.addTab("Tab " + str(i), None, panel, "Tooltip " + str(i))
        tabbedPane.setEnabledAt(4, False)

    @staticmethod            
    def main():
        app = TabsApp()
        app.make_ui()

TabsApp.main()

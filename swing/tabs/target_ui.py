from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent
from java.lang import System
class TabsApp:            
    def make_ui(self):
        frame = swing.JFrame("Tabs demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        frame.setPreferredSize(Dimension(300, 250))
        frame.add(self.createTabbedPane())
        frame.pack()
        frame.setVisible(True)

    def createTabbedPane(self):
        class TabSelectionListener(swing.event.ChangeListener):
            def stateChanged(listenerSelf, event):
                pane = event.getSource()
                index = pane.getSelectedIndex()
                # Shouldn't be visible, unless we're actually there
                pane.getComponentAt(0).getComponents()[0].setText("Edited")
                print pane.getTitleAt(index), "selected"
                
        tPane = swing.JTabbedPane(swing.JTabbedPane.TOP)
        self.addTabs(tPane)
        tPane.addChangeListener(TabSelectionListener())
        return tPane
    
    def addTabs(self, tabbedPane):
        for i in range(1, 6):
            panel = swing.JPanel()
            panel.add(swing.JLabel("content " + str(i)))
            tabbedPane.add("Tab " + str(i), panel)

    @staticmethod            
    def main():
        app = TabsApp()
        app.make_ui()

TabsApp.main()

from javax.swing import JFrame, JLabel, JSplitPane

class DemoApp: 
    def make_ui(self):
        frame = JFrame("Demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.getContentPane().add(self.getMainPane())
        frame.pack()
        frame.setVisible(True)

    def getMainPane(self):
        pane = JSplitPane(JSplitPane.VERTICAL_SPLIT)
        pane.setTopComponent(JLabel("The Top"))
        pane.setBottomComponent(self.getSubPane())
        return pane

    def getSubPane(self):
        pane = JSplitPane(JSplitPane.HORIZONTAL_SPLIT)
        pane.setLeftComponent(JLabel("The Left"))
        pane.setRightComponent(JLabel("The Right"))
        return pane

    @staticmethod        
    def main():
        app = DemoApp()
        app.make_ui()

DemoApp.main()

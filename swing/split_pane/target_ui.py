from javax import swing

class DemoApp: 
    def make_ui(self):
        frame = swing.JFrame("Demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.getContentPane().add(self.getMainPane())
        frame.pack()
        frame.setVisible(True)

    def getMainPane(self):
        pane = swing.JSplitPane(swing.JSplitPane.VERTICAL_SPLIT)
        pane.setTopComponent(swing.JLabel("The Top"))
        pane.setBottomComponent(self.getSubPane())
        return pane

    def getSubPane(self):
        pane = swing.JSplitPane(swing.JSplitPane.HORIZONTAL_SPLIT)
        pane.setLeftComponent(swing.JLabel("The Left"))
        pane.setRightComponent(swing.JLabel("The Right"))
        return pane

    @staticmethod        
    def main():
        app = DemoApp()
        app.make_ui()

DemoApp.main()

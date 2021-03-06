from java.awt import BorderLayout,BasicStroke, Color
from java.lang import System
from javax.swing import JFrame, JPanel, JButton, JToolBar, Icon

# Translated from Java example code
## @author Collin Fagan
## @date 7/25/2007
class RedCrossIcon(Icon):
    def __init__(self, size=32, description=""):
        self.width = size
        self.height = size
        self.stroke = BasicStroke(4)
        self.description = description

    def getDescription(self):
        return self.description

    def getIconWidth(self):
        return self.width

    def getIconHeight(self):
        return self.height

    def paintIcon(self, component, graphics, x, y):
        g2d = graphics.create()        
        g2d.setColor(Color.WHITE)
        g2d.fillRect(x +1 ,y + 1, self.width -2 ,self.height -2)
        
        g2d.setColor(Color.BLACK)
        g2d.drawRect(x +1 ,y + 1, self.width -2 ,self.height -2)
        
        g2d.setColor(Color.RED)
        
        g2d.setStroke(self.stroke)
        g2d.drawLine(x +10, y + 10, x + self.width -10, y + self.height -10)
        g2d.drawLine(x +10, y + self.height -10, x + self.width -10, y + 10)
        
        g2d.dispose()

# Just to check that we look for image equality...
class RedCrossIconWithImage(RedCrossIcon):
    def getImage(self):
        return 0


class ToolBarApp:
        
    def make_ui(self):
        frame = JFrame("Tool bar demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        panel = JPanel()
        #panel.setPreferredSize(Dimension(500, 100))
        panel.add(self.createToolBar())
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createToolBar(self):
        toolBar = JToolBar()
        self.addButtons(toolBar)
        return toolBar
    
    def addButtons(self, toolBar):
        icon = RedCrossIcon(32)
        button = JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item1")
        toolBar.add(button)

        button = JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item2")
        toolBar.add(button)

        icon = RedCrossIconWithImage(32)
        button = JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item3")
        toolBar.add(button)

        icon = RedCrossIconWithImage(32)
        button = JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item4")
        toolBar.add(button)

        icon = RedCrossIcon(32, "Has description")
        button = JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item5")
        toolBar.add(button)

        icon = RedCrossIcon(32, "Came from file:/some/path/image.gif")
        button = JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item6")
        toolBar.add(button)

    def printButton(self, event):
        widget = event.getSource()
        print "Selected Tool bar's", widget.getToolTipText()
        
    def quit(self, event):
        self.printMenu(event)
        System.exit(0)

    @staticmethod        
    def main():
        app = ToolBarApp()
        app.make_ui()

ToolBarApp.main()

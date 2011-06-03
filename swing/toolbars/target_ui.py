from javax import swing
from java.awt import BorderLayout, Dimension, BasicStroke, Color
from java.awt.event import KeyEvent
from java.lang import System

# Translated from Java example code
## @author Collin Fagan
## @date 7/25/2007
class RedCrossIcon(swing.Icon):
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
        frame = swing.JFrame("Tool bar demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        panel = swing.JPanel()
        #panel.setPreferredSize(Dimension(500, 100))
        panel.add(self.createToolBar())
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createToolBar(self):
        toolBar = swing.JToolBar()
        self.addButtons(toolBar)
        return toolBar
    
    def addButtons(self, toolBar):
        icon = RedCrossIcon(32)
        button = swing.JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item1")
        button.setName("Item1")
        toolBar.add(button)

        button = swing.JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item2")
        button.setName("Item2")
        toolBar.add(button)

        icon = RedCrossIconWithImage(32)
        button = swing.JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item3")
        button.setName("Item3")
        toolBar.add(button)

        icon = RedCrossIconWithImage(32)
        button = swing.JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item4")
        button.setName("Item4")
        toolBar.add(button)

        icon = RedCrossIcon(32, "Has description")
        button = swing.JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item5")
        button.setName("Item5")
        toolBar.add(button)

        icon = RedCrossIcon(32, "Came from file:/some/path/image.gif")
        button = swing.JButton(icon, actionPerformed=self.printButton)
        button.setToolTipText("Item6")
        button.setName("Item6")
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

from org.eclipse.draw2d import MouseMotionListener, MouseListener, RectangleFigure, Figure, FigureCanvas, Label, LineBorder, MarginBorder, ColorConstants, FigureUtilities
from org.eclipse.draw2d.geometry import Rectangle
from org.eclipse.swt import SWT
from org.eclipse.swt.graphics import Color as SwtColor
from org.eclipse.swt.widgets import Display, Shell
from org.eclipse.swt.layout import GridLayout, GridData
from java.awt import Color

class Dragger(MouseMotionListener, MouseListener):
    def __init__(self, figure):
        figure.addMouseMotionListener(self);
        figure.addMouseListener(self);
        self.lastPoint = None;
        
    def mouseReleased(self, e):
        pass          
    def mouseClicked(self, e):
        pass
    def mouseDoubleClicked(self, e):
        pass
    def mousePressed(self, e):
        self.lastPoint = e.getLocation()
        e.consume()

    def mouseEntered(self, e):
        pass
    def mouseExited(self, e):
        pass
    def mouseMoved(self, e):
        pass
    def mouseHover(self, e):
        pass
    def mouseDragged(self, e):
        p = e.getLocation()
        delta = p.getDifference(self.lastPoint)
        self.lastPoint = p
        f = e.getSource()
        f.setBounds(f.getBounds().getTranslated(delta.width(), delta.height()))

class TextRectangle(RectangleFigure):
    def __init__(self):
        RectangleFigure.__init__(self)
        self.texts = []
        self.rects = []

    def setText(self, text, x=2, y=2):
        self.texts.append((text, x, y))
    addText = setText

    def addRectangle(self, colour, *args):
        self.rects.append((colour, args))

    def paintFigure(self, graphics):
        RectangleFigure.paintFigure(self, graphics)
        loc = self.getLocation()
        for color, dimensions in self.rects:
            graphics.setBackgroundColor(color)
            x, y, width, height = dimensions
            graphics.fillRectangle(loc.x() + x, loc.y() + y, width, height)
        for text, x, y in self.texts:
            graphics.drawString(text, loc.x() + x, loc.y() + y)
        

def awtToSwtColor(awtColor):
    return SwtColor(Display.getDefault(), awtColor.getRed(), awtColor.getGreen(), awtColor.getBlue())

def createNode(x, y, color=None, border=True, cls=None, text=None, width=50, height=30):
    node1 = TextRectangle()
    if color:
        node1.setBackgroundColor(color)
    if text:
        node1.setText(text)
    node1.setBounds(Rectangle(x, y, width, height))
    if border:
        node1.setBorder(LineBorder())
    Dragger(node1)
    return node1
    
def getContents():
    panel = Figure()
    panel.setBounds(Rectangle(0,0,500,440))
    rect = createNode(40, 40, border=False, color=ColorConstants.yellow, text="topleft", width=100, height=160)
    rect.addText("topmid", x=50)
    rect.addText("centre", x=50, y=40)
    rect.addText("bottomleft", y=80)
    rect.addRectangle(ColorConstants.lightBlue, 0, 0, 50, 40)
    rect.addRectangle(ColorConstants.lightGreen, 50, 40, 50, 40)
    #rect.addRectangle(ColorConstants.yellow, 0, 40, 50, 40)
    rect.addRectangle(awtToSwtColor(Color.orange), 0, 40, 50, 40)
    rect.addRectangle(ColorConstants.orange, 0, 78, 50, 40)
    rect.addRectangle(ColorConstants.red, 50, 78, 50, 40)
    rect.addRectangle(FigureUtilities.lighter(ColorConstants.red), 0, 120, 50, 40)
    rect.addRectangle(FigureUtilities.darker(ColorConstants.orange), 50, 120, 50, 40)
    panel.add(rect)
    return panel

d = Display.getDefault();
shell = Shell(d, SWT.SHELL_TRIM)
shell.setText("Draw2d Application")
shell.setLayout(GridLayout(2, False))
figureCanvas = FigureCanvas(shell)
figureCanvas.setContents(getContents())
figureCanvas.getViewport().setContentsTracksHeight(True)
figureCanvas.getViewport().setContentsTracksWidth(True)
figureCanvas.setLayoutData(GridData(GridData.FILL_BOTH))   
figureCanvas.setSize(500,440)
shell.pack()
shell.open()
while not shell.isDisposed():
    if not d.readAndDispatch():
        d.sleep();
        
d.dispose()

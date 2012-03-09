from org.eclipse import draw2d
from org.eclipse.swt import SWT
from org.eclipse.swt.widgets import Display, Shell
from org.eclipse.swt.layout import GridLayout, GridData

class Dragger(draw2d.MouseMotionListener, draw2d.MouseListener):
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

class TextRectangle(draw2d.RectangleFigure):
    def __init__(self):
        draw2d.RectangleFigure.__init__(self)
        self.texts = []

    def setText(self, text, x=2, y=2):
        self.texts.append((text, x, y))
    addText = setText

    def paintFigure(self, graphics):
        draw2d.RectangleFigure.paintFigure(self, graphics)
        loc = self.getLocation()
        for text, x, y in self.texts:
            graphics.drawString(text, loc.x() + x, loc.y() + y) 

def createNode(x, y, color=None, border=True, cls=None, text=None, width=50, height=30):
    node1 = TextRectangle()
    if color:
        node1.setBackgroundColor(color)
    if text:
        node1.setText(text)
    node1.setBounds(draw2d.geometry.Rectangle(x, y, width, height))
    if border:
        node1.setBorder(draw2d.LineBorder())
    Dragger(node1)
    return node1
    
def getContents():
    panel = draw2d.Figure()
    panel.setBounds(draw2d.geometry.Rectangle(0,0,500,440))
    rect = createNode(40, 40, border=False, text="topleft", width=100, height=100)
    rect.addText("topmid", x=50)
    rect.addText("centre", x=50, y=40)
    rect.addText("bottomleft", y=80)
    panel.add(rect)
    rect = createNode(40, 160, border=True, text="00", width=100, height=100)
    rect.addText("10", x=50)
    rect.addText("11", x=50, y=40)
    rect.addText("02", y=80)
    panel.add(rect)
    label = draw2d.Label()
    label.setText("An extra label")
    label.setBounds(draw2d.geometry.Rectangle(40,400,500,40))
    panel.add(label)
    return panel

d = Display.getDefault();
shell = Shell(d, SWT.SHELL_TRIM)
shell.setText("Draw2d Application")
shell.setLayout(GridLayout(2, False))
figureCanvas = draw2d.FigureCanvas(shell)
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

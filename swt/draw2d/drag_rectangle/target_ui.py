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

def createNode(x, y, color=None, border=True, cls=None, text=None):
    actualCls = cls or draw2d.RectangleFigure
    node1 = actualCls()
    if color:
        node1.setBackgroundColor(color)
    if text:
        node1.setText(text)
    node1.setBounds(draw2d.geometry.Rectangle(x, y, 50, 30))
    if border:
        node1.setBorder(draw2d.LineBorder())
    Dragger(node1)
    return node1
    
def getContents():
    panel = draw2d.Figure()
    panel.setBounds(draw2d.geometry.Rectangle(0,0,500,440))
    panel.add(createNode(40, 40, border=False, cls=draw2d.Label, text="A longish label"))
    panel.add(createNode(40, 100, draw2d.ColorConstants.lightBlue))
    panel.add(createNode(100, 100, draw2d.ColorConstants.lightGreen))
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

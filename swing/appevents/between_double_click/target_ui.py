from javax.swing import JFrame, JPanel, JTable, JComponent,JScrollPane, ListSelectionModel
from javax.swing.table import DefaultTableModel
from java.awt import BorderLayout, Toolkit, Dimension, AWTEvent
from java.awt.event import MouseEvent, AWTEventListener

class ApplicationEvent(MouseEvent):
    def __init__(self, component, message):
        MouseEvent.__init__(self, component, MouseEvent.MOUSE_PRESSED, 0, 0, 0, 0, 0, False)
        self.message = message

    def getApplicationEventMessage(self):
        return self.message

class ApplicationEventManager(JComponent):
    instance = None
    
    def sendApplicationEvent(self, message):
        ev = ApplicationEvent(self, message)
        queue = Toolkit.getDefaultToolkit().getSystemEventQueue()
        currEvents = [ ev ]
        while queue.peekEvent():
            currEvents.append(queue.getNextEvent())
        for currEvent in currEvents:
            queue.postEvent(currEvent)


ApplicationEventManager.instance = ApplicationEventManager()

class MouseReleaseListener(AWTEventListener):
    def eventDispatched(self, event):
        if event.getID() == MouseEvent.MOUSE_RELEASED and event.getClickCount() == 1:
            ApplicationEventManager.instance.sendApplicationEvent("single click to be received")

class TableApp:        
    def make_ui(self):
        frame = JFrame("Table demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        scrollPane = JScrollPane()
        scrollPane.setPreferredSize(Dimension(300,100))
        scrollPane.getViewport().setView(self.createTable())
        panel = JPanel()
        panel.add(scrollPane)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        class myTable(JTable):
            def isCellEditable(self, rowIndex, colIndex):
                return False
    
        data = [ ['Tom'], ['Dick'], ['Harry'] ]
        columns = ("Name",)
        model = DefaultTableModel(data, columns)
        table = myTable(model)
        table.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        Toolkit.getDefaultToolkit().addAWTEventListener(MouseReleaseListener(), AWTEvent.MOUSE_EVENT_MASK)
        return table
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

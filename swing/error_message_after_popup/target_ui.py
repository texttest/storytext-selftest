from javax import swing
from javax.swing import JFrame, JPanel, JButton, JOptionPane, JTable, JScrollPane, JTabbedPane, JPopupMenu, \
    AbstractAction, ListSelectionModel, TransferHandler
from javax.swing.table import DefaultTableModel
from java.awt import BorderLayout, Dimension
from java.awt.event import MouseAdapter
from javax.naming import OperationNotSupportedException

class TableTransferHandler(TransferHandler):
    def importData(self, component, transferable):
        try:
            print "Transfering"
            self.doImport()
        except OperationNotSupportedException, ex:
            ex.printStackTrace()
            JOptionPane.showMessageDialog(None, ex.getMessage())
        return False

    def doImport(self):
        raise OperationNotSupportedException("Error: Operation not supported exception")

class PopupListener(MouseAdapter):
    def __init__(self, popup):
        self.popupMenu = popup

    def mousePressed(self, event):
        self.showPopup(event)
        
    def mousereleased(self, event):
        self.showPopup(event)
        
    def showPopup(self, event):
        if event.isPopupTrigger():
            self.popupMenu.show(event.getComponent(), event.getX(), event.getY())

class PasteAction(AbstractAction):
    def __init__(self, table):
        AbstractAction.__init__(self,"Paste")
        self.table = table

    def actionPerformed(self, event):
        self.table.getTransferHandler().importData(self.table, None)


class TabCloseAction(AbstractAction):
    def __init__(self, name, tab):
        AbstractAction.__init__(self, name)
        self.tab = tab
        
    def actionPerformed(self, event):
        index = self.tab.getSelectedIndex()
        self.tab.remove(index)
        
class TableApp:
        
    def make_ui(self):
        frame = JFrame("Popup demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        scrollPane = JScrollPane()
        scrollPane.setPreferredSize(Dimension(300,100))
        table = self.createTable()
        table.addMouseListener(PopupListener(self.createTablePopup(table)))
        table.setTransferHandler(TableTransferHandler())
        tabbedPane = JTabbedPane(JTabbedPane.TOP)
        tabbedPane.addMouseListener(PopupListener(self.createTabPopup(tabbedPane)))
        panel = JPanel()
        tabbedPane.add("Persons", table)
        tabbedPane.add("Nothing", JPanel())
        scrollPane.getViewport().setView(tabbedPane)
        
        panel.add(scrollPane)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        data = [
                ['Anders', '21' ,'male'],
                ['Eva', '22', 'female'],
                ]
        columns = ("Name", "Age", "Gender")
        model = DefaultTableModel(data, columns)
        table = JTable(model)
        table.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        return table

    def createTablePopup(self, table):
        popup = JPopupMenu();
        popup.add(PasteAction(table))
        return popup
    
    def createTabPopup(self, pane):
        popup = JPopupMenu();
        popup.add(TabCloseAction("Close", pane))
        return popup
                
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

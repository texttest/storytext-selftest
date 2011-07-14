from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent, MouseAdapter

class PopupListener(MouseAdapter):
    def __init__(self, popup):
        self.popupMenu = popup

    def mousePressed(self, event):
        self.showPopup(event)
        
    def mousereleased(self, event):
        self.showPopup(event)
        
    def showPopup(self, event):
        if event.isPopupTrigger():
            self.popupMenu.show(event.getComponent(), event.getX(), event.getY());

class InsertAction(swing.AbstractAction):
    def __init__(self, name, table):
        swing.AbstractAction.__init__(self, name)
        self.table = table
        
    def actionPerformed(self, event):
        self.table.getModel().addRow(['', '' ,''])

class TabCloseAction(swing.AbstractAction):
    def __init__(self, name, tab):
        swing.AbstractAction.__init__(self, name)
        self.tab = tab
        
    def actionPerformed(self, event):
        index = self.tab.getSelectedIndex()
        self.tab.remove(index)
        
class TableApp:
        
    def make_ui(self):
        frame = swing.JFrame("Popup demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        scrollPane = swing.JScrollPane()
        scrollPane.setPreferredSize(Dimension(300,100))
        table = self.createTable()
        table.addMouseListener(PopupListener(self.createTablePopup(table)))
        tabbedPane = swing.JTabbedPane(swing.JTabbedPane.TOP)
        tabbedPane.addMouseListener(PopupListener(self.createTabPopup(tabbedPane)))
        panel = swing.JPanel()
        tabbedPane.add("Persons", table)
        tabbedPane.add("Nothing", swing.JPanel())
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
        model = swing.table.DefaultTableModel(data, columns)
        table = swing.JTable(model)
        table.setSelectionMode(swing.ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        return table

    def createTablePopup(self, table):
        popup = swing.JPopupMenu();
        popup.add(InsertAction("Insert row", table))
        return popup
    
    def createTabPopup(self, pane):
        popup = swing.JPopupMenu();
        popup.add(TabCloseAction("Close", pane))
        return popup
                
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()


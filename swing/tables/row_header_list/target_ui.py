from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent

class TableApp:
        
    def make_ui(self):
        frame = swing.JFrame("Table demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        scrollPane = swing.JScrollPane()
        scrollPane.setPreferredSize(Dimension(300,100))
        self.table = self.createTable()
        scrollPane.getViewport().setView(self.table)
        jlist = swing.JList(range(1, 4))

        class ListSelectionListener(swing.event.ListSelectionListener):
            def valueChanged(listenerSelf, event):
                self.table.changeSelection(event.getFirstIndex(), 0, False, False)
                
        jlist.addListSelectionListener(ListSelectionListener())
        scrollPane.setRowHeaderView(jlist)
        panel = swing.JPanel()
        panel.add(scrollPane)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        data = [ ['Tom'], ['Dick'], ['Harry'] ]
        columns = ("Name",)
        model = swing.table.DefaultTableModel(data, columns)
        table = swing.JTable(model)
        table.setSelectionMode(swing.ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        return table

    def createList(self):
        return swing.JList(range(1, 4))
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent

class TableApp:
        
    def make_ui(self):
        frame = swing.JFrame("Table demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        panel = swing.JPanel()
        scrollPane = swing.JScrollPane()
        self.table = self.createTable()
        jlist = swing.JList(range(1, 4))
        panel.add(jlist)
        panel.add(self.table)
        scrollPane.setColumnHeaderView(self.table.getTableHeader())
        scrollPane.getViewport().setView(panel)

        class ListSelectionListener(swing.event.ListSelectionListener):
            def valueChanged(listenerSelf, event):
                if event.getValueIsAdjusting():
                    return
                self.table.addRowSelectionInterval(event.getFirstIndex(), event.getFirstIndex())
                for column in range(self.table.getColumnCount()):
                    self.table.changeSelection(event.getFirstIndex(), column, False, True)
                
        jlist.addListSelectionListener(ListSelectionListener())
        scrollPane.setRowHeaderView(jlist)
        
        panel.setOpaque(True)
        frame.getContentPane().add(scrollPane, BorderLayout.CENTER)
        frame.setPreferredSize(Dimension(300,100))
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        data = [ ['Tom'] * 20, ['Dick'] * 20, ['Harry'] * 20 ]
        columns = tuple([ "Name" + str(i) for i in range(1, 21) ])
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

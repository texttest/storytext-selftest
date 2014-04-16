from java.awt import BorderLayout, Dimension
from javax.swing import JFrame, JScrollPane, JPanel, JTable, JList, ListSelectionModel
from javax.swing.event import ListSelectionListener
from javax.swing.table import DefaultTableModel

class TableApp:
        
    def make_ui(self):
        frame = JFrame("Table demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        scrollPane = JScrollPane()
        scrollPane.setPreferredSize(Dimension(300,100))
        self.table = self.createTable()
        scrollPane.getViewport().setView(self.table)
        jlist = JList(range(1, 4))

        class MyListSelectionListener(ListSelectionListener):
            def valueChanged(listenerSelf, event):
                self.table.changeSelection(event.getFirstIndex(), 0, False, False)
                
        jlist.addListSelectionListener(MyListSelectionListener())
        scrollPane.setRowHeaderView(jlist)
        panel = JPanel()
        panel.add(scrollPane)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        data = [ ['Tom'] * 20, ['Dick'] * 20, ['Harry'] * 20 ]
        columns = tuple([ "Name" + str(i) for i in range(1, 21) ])
        model = DefaultTableModel(data, columns)
        table = JTable(model)
        table.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        return table

    def createList(self):
        return JList(range(1, 4))
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

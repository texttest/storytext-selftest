from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import KeyEvent
from javax.swing import JFrame, JScrollPane, JPanel, JTable, JList, ListSelectionModel
from javax.swing.event import ListSelectionListener
from javax.swing.table import DefaultTableModel

class TableApp:
        
    def make_ui(self):
        frame = JFrame("Table demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        panel = JPanel()
        scrollPane = JScrollPane()
        self.table = self.createTable()
        jlist = JList(range(1, 4))
        panel.add(jlist)
        panel.add(self.table)
        scrollPane.setColumnHeaderView(self.table.getTableHeader())
        scrollPane.getViewport().setView(panel)

        class MyListSelectionListener(ListSelectionListener):
            def valueChanged(listenerSelf, event):
                if event.getValueIsAdjusting():
                    return
                self.table.addRowSelectionInterval(event.getFirstIndex(), event.getFirstIndex())
                for column in range(self.table.getColumnCount()):
                    self.table.changeSelection(event.getFirstIndex(), column, False, True)
                
        jlist.addListSelectionListener(MyListSelectionListener())
        scrollPane.setRowHeaderView(jlist)
        
        panel.setOpaque(True)
        frame.getContentPane().add(scrollPane, BorderLayout.CENTER)
        frame.setPreferredSize(Dimension(300,100))
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

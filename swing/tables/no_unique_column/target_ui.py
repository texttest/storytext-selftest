from javax import swing
from java.awt import BorderLayout, Dimension
from java.awt.event import MouseAdapter

class MyTableModel(swing.table.DefaultTableModel):
    def isCellEditable(self, row, col):
        return col != 2


class TableApp:
        
    def make_ui(self):
        frame = swing.JFrame("Table demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        scrollPane = swing.JScrollPane()
        scrollPane.setPreferredSize(Dimension(300,100))
        scrollPane.getViewport().setView(self.createTable())
        panel = swing.JPanel()
        panel.add(scrollPane)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        data = [
                ['Human', 'Anders', '21' ,'male'],
                ['Human', 'Anders', '22' ,'male'],
                ['Human', 'Eva', '22', 'female'],
                ]
        columns = ("Species", "Name", "Age", "Gender")
        model = MyTableModel(data, columns)
        table = swing.JTable(model)
        table.setSelectionMode(swing.ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        return table
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

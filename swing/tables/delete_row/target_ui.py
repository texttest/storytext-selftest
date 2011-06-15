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
        button = swing.JButton("Delete", actionPerformed=self.deleteRow)
        panel = swing.JPanel()
        panel.add(button)
        panel.add(scrollPane)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        data = [
                ['Person', 'Anders', '21' ,'male'],
                ['Person', 'Eva', '22', 'female'],
                ]
        columns = ("Type", "Name", "Age", "Gender")
        self.model = swing.table.DefaultTableModel(data, columns)
        table = swing.JTable(self.model)
        table.setSelectionMode(swing.ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        return table

    def deleteRow(self, *args):
        self.model.removeRow(1)
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

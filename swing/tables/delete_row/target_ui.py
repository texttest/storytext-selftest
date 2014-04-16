from java.awt import BorderLayout, Dimension
from javax.swing import JFrame, JScrollPane, JPanel, JTable, JButton, ListSelectionModel
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
        button = JButton("Delete", actionPerformed=self.deleteRow)
        panel = JPanel()
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
        self.model = DefaultTableModel(data, columns)
        table = JTable(self.model)
        table.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        return table

    def deleteRow(self, *args):
        self.model.removeRow(1)
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

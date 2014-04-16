from java.awt import BorderLayout, Dimension
from javax.swing import JFrame, JScrollPane, JPanel, JButton, JTable, ListSelectionModel
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
        button = JButton("Add Rows", actionPerformed=self.addRows)
        panel = JPanel()
        panel.add(button)
        panel.add(scrollPane)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        data = [
                ]
        columns = ("Type", "Name", "Age", "Gender")
        self.model = DefaultTableModel(data, columns)
        table = JTable(self.model)
        table.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        return table

    def addRows(self, *args):
        self.model.addRow(['Person', 'Anders', '21' ,'male'])
        self.model.addRow(['Person', 'Eva', '22', 'female'])
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

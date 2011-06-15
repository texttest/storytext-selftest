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
        button = swing.JButton("Add Rows", actionPerformed=self.addRows)
        panel = swing.JPanel()
        panel.add(button)
        panel.add(scrollPane)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        data = [
                ]
        columns = ("Type", "Name", "Age", "Gender")
        self.model = swing.table.DefaultTableModel(data, columns)
        table = swing.JTable(self.model)
        table.setSelectionMode(swing.ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
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

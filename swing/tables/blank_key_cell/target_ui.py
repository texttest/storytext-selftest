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
        scrollPane.getViewport().setView(self.createTable())
        panel = swing.JPanel()
        panel.add(scrollPane)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        data = [
                ['Anders', '21' ,'male'],
                ['', '22', 'female'],
                ]
        columns = ("Name", "Age", "Gender")
        model = swing.table.DefaultTableModel(data, columns)
        table = swing.JTable(model)
        table.setSelectionMode(swing.ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        return table
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

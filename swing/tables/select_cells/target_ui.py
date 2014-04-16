from java.awt import BorderLayout, Dimension
from java.awt.event import MouseAdapter
from javax.swing import JFrame, JScrollPane, JPanel, JTable, ListSelectionModel
from javax.swing.table import DefaultTableModel

class MyTableModel(DefaultTableModel):
    def isCellEditable(self, row, col):
        return col != 2


class TableApp:
        
    def make_ui(self):
        frame = JFrame("Table demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        scrollPane = JScrollPane()
        scrollPane.setPreferredSize(Dimension(300,100))
        scrollPane.getViewport().setView(self.createTable())
        panel = JPanel()
        panel.add(scrollPane)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createTable(self):
        data = [
                ['Anders', '21' ,'male'],
                ['Eva', '22', 'female'],
                ]
        columns = ("Name", "Age", "Gender")
        model = MyTableModel(data, columns)
        table = JTable(model)
        table.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        class PrintListener(MouseAdapter):
            def mousePressed(self, e):
                if e.getClickCount() == 2:
                    print "Got double-click!"

        table.addMouseListener(PrintListener())
        return table
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

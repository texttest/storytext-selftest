from java.awt import BorderLayout, Dimension
from javax.swing import JFrame, JScrollPane, JPanel, JTable, ListSelectionModel
from javax.swing.table import DefaultTableModel, DefaultTableCellRenderer

class MyRenderer(DefaultTableCellRenderer):
    def getTableCellRendererComponent(self, widget, value, *args):
        component = DefaultTableCellRenderer.getTableCellRendererComponent(self, widget, value, *args)
        component.setText("Rendered " + value)
        return component


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
        model = DefaultTableModel(data, columns)
        table = JTable(model)
        table.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        table.getColumnModel().getColumn(0).setCellRenderer(MyRenderer())
        return table
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

from java.awt import BorderLayout, Dimension
from java.awt.event import ActionListener, MouseEvent
from javax.swing import JFrame, JScrollPane, JPanel, JTable, JTextField, ListSelectionModel, AbstractCellEditor
from javax.swing.table import DefaultTableModel, TableCellEditor

class CustomCellEditor(AbstractCellEditor, TableCellEditor, ActionListener):
    def __init__(self):
        self.editorComponent = JTextField()
        self.editorComponent.addActionListener(self)
        
    def getTableCellEditorComponent(self, table, value, isSelected, rowIndex, vColIndex):
        self.editorComponent.setText(value)
        return self.editorComponent
    
    def getCellEditorValue(self):
        return self.editorComponent.getText()

    def actionPerformed(self, event):
        self.stopCellEditing()

    def isCellEditable(self, event):
        if isinstance(event, MouseEvent):
            return event.getClickCount() >= 2

        return True

    
class CustomEditorApp:
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
        data = [ ['Tom', '22'], ['Dick', '23'], ['Harry', '24'] ]
        columns = ("Name", "Age")
        model = DefaultTableModel(data, columns)
        table = JTable(model)
        table.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        col = table.getColumnModel().getColumn(1)
        col.setCellEditor(CustomCellEditor())
        return table
    
    @staticmethod                    
    def main():
        app = CustomEditorApp()
        app.make_ui()
        
CustomEditorApp.main()

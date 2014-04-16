from java.awt import GridLayout, Dimension
from javax.swing import JFrame, JScrollPane, JPanel, JTable, JButton, BoxLayout, ListSelectionModel
from javax.swing.table import DefaultTableModel, TableRowSorter

class TableApp:
        
    def make_ui(self):
        frame = JFrame("Table demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BoxLayout(frame.getContentPane(), BoxLayout.PAGE_AXIS))
        scrollPane = JScrollPane()
        scrollPane.setPreferredSize(Dimension(300,100))
        self.table = self.createTable()
        scrollPane.getViewport().setView(self.table)
        buttonPanel = JPanel(GridLayout())
        button0 = self.createButton("Remove Name", "Name")
        button1 = self.createButton("Remove Age", "Age")
        button2 = self.createButton("Remove Gender", "Gender")
        buttonPanel.add(button0)
        buttonPanel.add(button1)
        buttonPanel.add(button2)
        panel = JPanel()
        panel.add(scrollPane)
        frame.add(buttonPanel)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createButton(self, name, action):
        button = JButton(name, actionPerformed=self.handleButton)
        button.setActionCommand(action)
        return button

    def handleButton(self, event):
        button = event.getSource()
        button.setEnabled(False)
        column = self.table.getColumn(button.getActionCommand())
        self.table.removeColumn(column)

    def createTable(self):
        data = [
                ['Eva', '22', 'female'],
                ['Anika', '31' ,'female'],
                ['Anna', '25' ,'female'],
                ['Anders', '21' ,'male'],
                ]
        columns = ("Name", "Age", "Gender")
        model = DefaultTableModel(data, columns)
        table = JTable(model)
        table.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        sorter = TableRowSorter(table.getModel())
        table.setRowSorter(sorter)
        table.setName("Persons")
        return table
            
    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

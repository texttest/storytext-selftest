from javax import swing
from java.awt import GridLayout, Dimension
from java.awt.event import KeyEvent

class TableApp:
        
    def make_ui(self):
        frame = swing.JFrame("Table demo")
        frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(swing.BoxLayout(frame.getContentPane(), swing.BoxLayout.PAGE_AXIS))
        scrollPane = swing.JScrollPane()
        scrollPane.setPreferredSize(Dimension(300,100))
	self.table = self.createTable()
        scrollPane.getViewport().setView(self.table)
	buttonPanel = swing.JPanel(GridLayout())
	button0 = self.createButton("Remove Name", "Name")
	button1 = self.createButton("Remove Age", "Age")
	button2 = self.createButton("Remove Gender", "Gender")
	buttonPanel.add(button0)
	buttonPanel.add(button1)
	buttonPanel.add(button2)
        panel = swing.JPanel()
        panel.add(scrollPane)
	frame.add(buttonPanel)
        frame.add(panel)
        frame.pack()
        frame.setVisible(True)

    def createButton(self, name, action):
	button = swing.JButton(name, actionPerformed=self.handleButton)
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
        model = swing.table.DefaultTableModel(data, columns)
        table = swing.JTable(model)
        table.setSelectionMode(swing.ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        table.setCellSelectionEnabled(True)
        sorter = swing.table.TableRowSorter(table.getModel())
        table.setRowSorter(sorter)
        table.setName("Persons")
        return table
            
    def printCells(self, event):
        widget = event.getSource()
        print "Selected Tool bar's",widget.getText(), "button"

    @staticmethod            
    def main():
        app = TableApp()
        app.make_ui()

TableApp.main()

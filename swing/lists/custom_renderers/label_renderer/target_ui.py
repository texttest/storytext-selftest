from javax.swing import JLabel, JPanel, JFrame, JList, JScrollPane, ListSelectionModel, ListCellRenderer
from java.awt import BorderLayout

class LabelListRenderer(JLabel, ListCellRenderer):
    def __init__(self):
        self.setOpaque(True)

    def getListCellRendererComponent(self, list,value, index, isSelected, cellHasFocus):
        self.setText(value)
        self.setEnabled(True)
        list.setEnabled(True)
        self.setBackground(list.getSelectionBackground() if isSelected else list.getBackground())
        self.setForeground(list.getSelectionForeground() if isSelected else list.getForeground())
        return self

class LabelListApp:
        
    def make_ui(self):
        frame = JFrame("List box Demo")
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setLayout(BorderLayout())
        newContentPane = JPanel()
        listData = [ "Item 1", "Item 2", "Item 3", "Item 4" ]
        list = JList(listData)
        list.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
        list.setCellRenderer(LabelListRenderer())

        newContentPane.add(JScrollPane(list), BorderLayout.CENTER);
        frame.add(newContentPane)
        frame.pack()
        frame.setVisible(True)

    def printButton(self, event):
        widget = event.getSource()
        if widget.isSelected():
            print "Selected the", widget.getText(), "check box"
        else:
            print "Deselected the", widget.getText(), "check box"

    @staticmethod            
    def main():
        app = LabelListApp()
        app.make_ui()

LabelListApp.main()


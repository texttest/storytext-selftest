
from javax.swing import JPanel, JFrame, JList, JScrollPane, DefaultListCellRenderer
from java import awt

frame = JFrame("List demo")
frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
frame.setTitle("List box Demo")
panel = JPanel()
panel.setPreferredSize(awt.Dimension(200, 60))
panel.setLayout(awt.BorderLayout())
frame.getContentPane().add(panel)

class MyRenderer(DefaultListCellRenderer):
    def getListCellRendererComponent(self, widget, value, *args):
        component = DefaultListCellRenderer.getListCellRendererComponent(self, widget, value, *args)
        component.setText("Rendered " + value)
        return component
        
listData = [ "Item 1", "Item 2", "Item 3", "Item 4" ]
list = JList(listData)
list.setCellRenderer(MyRenderer())

panel.add(JScrollPane(list), awt.BorderLayout.CENTER);
frame.pack()
frame.setVisible(True)

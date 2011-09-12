
from javax import swing
from java import awt

frame = swing.JFrame("List demo")
frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
frame.setTitle("List box Demo")
panel = swing.JPanel()
panel.setPreferredSize(awt.Dimension(200, 60))
panel.setLayout(awt.BorderLayout())
frame.getContentPane().add(panel)

class MyRenderer(swing.DefaultListCellRenderer):
    def getListCellRendererComponent(self, widget, value, *args):
        component = swing.DefaultListCellRenderer.getListCellRendererComponent(self, widget, value, *args)
        component.setText("Rendered " + value)
        return component
        
listData = [ "Item 1", "Item 2", "Item 3", "Item 4" ]
list = swing.JList(listData)
list.setCellRenderer(MyRenderer())

panel.add(swing.JScrollPane(list), awt.BorderLayout.CENTER);
frame.pack()
frame.setVisible(True)

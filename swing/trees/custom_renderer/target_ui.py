
from javax import swing
from java import awt

def createNodes():
    top = swing.tree.DefaultMutableTreeNode("The Java Series")

    category = swing.tree.DefaultMutableTreeNode("Books for Java Programmers")
    top.add(category)

    book = swing.tree.DefaultMutableTreeNode("The Java Tutorial")
    category.add(book)

    book = swing.tree.DefaultMutableTreeNode("The Java Tutorial Continued")
    category.add(book)

    category = swing.tree.DefaultMutableTreeNode("Books for Java Implementers")
    top.add(category)

    book = swing.tree.DefaultMutableTreeNode("The Java Virtual Machine Specification")
    category.add(book)

    book = swing.tree.DefaultMutableTreeNode("The Java Language Specification")
    category.add(book)
    return top


frame = swing.JFrame("Tree demo")
frame.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
frame.setTitle("Tree Demo")
panel = swing.JPanel()
panel.setPreferredSize(awt.Dimension(200, 60))
panel.setLayout(awt.BorderLayout())
frame.getContentPane().add(panel)

class MyRenderer(swing.tree.DefaultTreeCellRenderer):
    def getTreeCellRendererComponent(self, widget, value, *args):
        component = swing.tree.DefaultTreeCellRenderer.getTreeCellRendererComponent(self, widget, value, *args)
        component.setText("Rendered " + str(value))
        return component
        
tree = swing.JTree(createNodes())
tree.setCellRenderer(MyRenderer())

panel.add(swing.JScrollPane(tree), awt.BorderLayout.CENTER);
frame.pack()
frame.setSize(500, 300)
frame.setVisible(True)

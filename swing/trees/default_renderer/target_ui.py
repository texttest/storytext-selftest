from java.awt import BorderLayout, Dimension
from javax.swing import JFrame, JPanel, JScrollPane, JTree
from javax.swing.tree import DefaultMutableTreeNode

def createNodes():
    top = DefaultMutableTreeNode("The Java Series")

    category = DefaultMutableTreeNode("Books for Java Programmers")
    top.add(category)

    book = DefaultMutableTreeNode("The Java Tutorial")
    category.add(book)

    book = DefaultMutableTreeNode("The Java Tutorial Continued")
    category.add(book)

    category = DefaultMutableTreeNode("Books for Java Implementers")
    top.add(category)

    book = DefaultMutableTreeNode("The Java Virtual Machine Specification")
    category.add(book)

    book = DefaultMutableTreeNode("The Java Language Specification")
    category.add(book)
    return top


frame = JFrame("Tree demo")
frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
frame.setTitle("Tree Demo")
panel = JPanel()
panel.setPreferredSize(Dimension(200, 60))
panel.setLayout(BorderLayout())
frame.getContentPane().add(panel)
        
tree = JTree(createNodes())
tree.setSelectionRow(1)

panel.add(JScrollPane(tree), BorderLayout.CENTER);
frame.pack()
frame.setSize(500, 300)
frame.setVisible(True)

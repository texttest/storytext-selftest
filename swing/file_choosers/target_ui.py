from java.awt import BorderLayout, Insets
from java.awt.event import ActionListener
from java.lang import Runnable
from javax.swing import JFrame, JPanel, JButton, JFileChooser, JTextArea, JScrollPane, SwingUtilities, UIManager

# FileChooserDemo.java uses these files:
#   images/Open16.gif
#   images/Save16.gif

class FileChooserDemo(JPanel, ActionListener):
    def __init__(self):
        JPanel.__init__(self, BorderLayout())

        #Create the log first, because the action listeners
        #need to refer to it.
        self.log = JTextArea(5,20)
        self.log.setMargin(Insets(5,5,5,5))
        self.log.setEditable(False)
        logScrollPane = JScrollPane(self.log)

        #Create a file chooser
        self.fc = JFileChooser("usecases")

        #Uncomment one of the following lines to try a different
        #file selection mode.  The first allows just directories
        #to be selected (and, at least in the Java look and feel,
        #shown).  The second allows both files and directories
        #to be selected.  If you leave these lines commented out,
        #then the default mode (FILES_ONLY) will be used.
        #
        #fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)
        #fc.setFileSelectionMode(JFileChooser.FILES_AND_DIRECTORIES)

        #Create the open button.  We use the image from the JLF
        #Graphics Repository (but we extracted it from the jar).
        self.openButton = JButton("Open a File...")
        self.openButton.addActionListener(self)

        #Create the save button.  We use the image from the JLF
        #Graphics Repository (but we extracted it from the jar).
        self.saveButton = JButton("Save a File...")
        self.saveButton.addActionListener(self)

        #For layout purposes, put the buttons in a separate panel
        buttonPanel = JPanel() #use FlowLayout
        buttonPanel.add(self.openButton)
        buttonPanel.add(self.saveButton)

        #Add the buttons and the log to self panel.
        self.add(buttonPanel, BorderLayout.PAGE_START)
        self.add(logScrollPane, BorderLayout.CENTER)

    def actionPerformed(self, e):
        #Handle open button action.
        if (e.getSource() == self.openButton):
            returnVal = self.fc.showOpenDialog(self)

            if (returnVal == JFileChooser.APPROVE_OPTION):
                file = self.fc.getSelectedFile()
                #Self is where a real application would open the file.
                self.log.append("Opening: " + file.getName() + ".\n")
            else:
                self.log.append("Open command cancelled by user.\n")
    
            self.log.setCaretPosition(self.log.getDocument().getLength())

        #Handle save button action.
        elif (e.getSource() == self.saveButton):
            returnVal = self.fc.showSaveDialog(self)
            if (returnVal == JFileChooser.APPROVE_OPTION):
                file = self.fc.getSelectedFile()
                #Self is where a real application would save the file.
                self.log.append("Saving: " + file.getName() + ".\n")
            else:
                self.log.append("Save command cancelled by user.\n")

            self.log.setCaretPosition(self.log.getDocument().getLength())

    # Create the GUI and show it.  For thread safety,
    #self method should be invoked from the
    # event dispatch thread.
    @staticmethod
    def createAndShowGUI():
        #Create and set up the window.
        frame = JFrame("FileChooserDemo")
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)

        #Add content to the window.
        frame.add(FileChooserDemo())

        #Display the window.
        frame.pack()
        frame.setVisible(True)


if __name__ == "__main__":
    #Schedule a job for the event dispatch thread:
    #creating and showing self application's GUI.
    class MyRunnable(Runnable):
        def run(self):
            #Turn off metal's use of bold fonts
            UIManager.put("swing.boldMetal", False) 
            FileChooserDemo.createAndShowGUI()

    SwingUtilities.invokeLater(MyRunnable())

import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JFrame;
import java.awt.BorderLayout;
import java.awt.Dimension;
/*
 * 
 * SINGLE_SELECTION = 0
 * SINGLE_INTERVAL_SELECTION = 1
 * MULTIPLE_INTERVAL_SELECTION = 2 (Default)
 *
 */

public class TargetUI extends JFrame {

	private static final long serialVersionUID = 4766653969900264715L;

	private String listData[] = { "Item 1", "Item 2", "Item 3", "Item 4" };

	public TargetUI(int selectionMode) {
		super("List demo");
		setDefaultCloseOperation(DISPOSE_ON_CLOSE);
		setTitle("List box Demo");
		JPanel panel = new JPanel();
		panel.setPreferredSize(new Dimension(200, 60));
		panel.setLayout(new BorderLayout());
		getContentPane().add(panel);
		//Default selection
		JList list = new JList(listData);
		if (selectionMode == 0 || selectionMode == 1)
			list.setSelectionMode(selectionMode);
		panel.add(new JScrollPane(list), BorderLayout.CENTER);
	}

	public static void main(String args[]) {
		TargetUI app = new TargetUI(args.length == 2 && args[1] != null && args[1] != "" ? Integer.valueOf(args[0]) : 2);
		app.pack();
		app.setVisible(true);
	}

}

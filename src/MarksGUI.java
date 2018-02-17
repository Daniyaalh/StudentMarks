import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridBagLayout;

import javax.swing.*;

public class MarksGUI {
	public static void showGUI() {
	JFrame frame = new JFrame("Marks Keeper");
	

	frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	frame.getContentPane().setLayout(new GridBagLayout());
	frame.getContentPane().setBackground(Color.white);
	frame.setSize(750,800);
	frame.setResizable(true);
	frame.setVisible(true);
	
	
	JPanel begin = new JPanel();
	//begin.setSize(600, 300);
	
	//JButton enterButton = new JButton("Enter");
	//enterButton.setSize(100, 100);
	//JLabel space = new JLabel("");
	//space.setFont(new Font("Serif", Font.BOLD, 100));
	JLabel logo = new JLabel("Marks Keeper");
	logo.setFont(new Font("Serif", Font.BOLD,75));
	begin.setLayout(new FlowLayout(0, 20, 40));
	
	JTextField passwordbox = new JTextField();
	passwordbox.setBounds(50, 50, 50, 50);
	
	//begin.add(space);
	begin.add(logo);
	//begin.add(enterButton);
	begin.add(passwordbox);
	begin.
	frame.add(begin);
	//frame.pack();
	}
	
	
public static void main(String[] args) {	
		
		javax.swing.SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				showGUI();
			}
		});
}
}
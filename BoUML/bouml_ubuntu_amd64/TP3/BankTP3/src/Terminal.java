import javax.swing.JFrame;
import javax.swing.JLabel;

class Terminal extends JFrame implements IObservateur {

  private JLabel message;

  public Terminal(String title) {
    super(title);
    this.setSize(400, 200);
    this.message = new JLabel("Compte ok");
    this.add(this.message);
    this.setVisible(true);
    this.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
  }

  @Override
  public void notification(String info) {
    this.message.setText(info);
  }

  

}

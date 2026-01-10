public class X implements IEvent {
    
  private Automate controleur;


  public X(){
    controleur = new Automate(this);
  }

    
  public Automate getControleur() {
        return controleur;
    }

  public void action1() {
    System.out.println("action1");

  }

  public void action2() {
    System.out.println("action2");
  }

  @Override
  public void event1() {
    getControleur().event1();
  }

  @Override
  public void event2() {
    getControleur().event2();
  }
}

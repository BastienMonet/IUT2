
class Automate implements IEvent {
  private IEtat e ;
  private X controle;

  public Automate(X control) {
    this.e = new Etat1();
    this.controle = control;

  }

  public X getControle() {
    return controle;
  }

  public void setEtatCourant(IEtat etat) {
    this.e = etat;
  }



  @Override
  public void event1() {
    this.e.event1(this);
  }

  @Override
  public void event2() {
    this.e.event2(this);
  }

}

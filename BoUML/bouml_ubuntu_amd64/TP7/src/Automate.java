
class Automate implements IEvent {
  private IEtat e;

  private Chrono controle;

  public Automate(Chrono control) {
    this.e = new Arret();
    this.controle = control;

  }

  public Chrono getControle() {
    return controle;
  }

  public void setEtatCourant(IEtat etat) {
    this.e = etat;
  }

  @Override
  public void go() {
    e.go(this);
  }

  @Override
  public void stop() {
    e.stop(this);
  }

}

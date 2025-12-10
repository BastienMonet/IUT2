
class Transition {
  private Etat etatFinal;

  private char symbole;

  public Transition(Etat etatFinal, char symbole) {
    this.etatFinal = etatFinal;
    this.symbole = symbole;
  }

  public final char getSymbole() {
    return symbole;
  }

  public Etat getEtatFinal() {
    return etatFinal;
  }

}

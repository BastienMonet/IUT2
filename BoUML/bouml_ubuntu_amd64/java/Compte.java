
class Compte {
  private double solde;

  private String numero;

  private double decouvertAutorise;


  public Compte(String numero) {
    this.numero = numero;
    this.solde = 0.0;
    this.decouvertAutorise = 0.0;
  }


  public final double getSolde() {
    return solde;
  }

  public void setSolde(double value) {
    solde = value;
  }

  public final double getDecouvertAutorise() {
    return decouvertAutorise;
  }

  public void setDecouvertAutorise(double value) {
    decouvertAutorise = value;
  }

  public final String getNumero() {
    return numero;
  }

  public void setNumero(String value) {
    numero = value;
  }

  public void crediter(float montant) {
  }

  public void debiter(float montant) {
  }


}

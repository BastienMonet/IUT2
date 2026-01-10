
class Nombre extends Operation {
  private float valeur;

  public Nombre(float valeur) {
    super();
    this.valeur = valeur;
  }

  @Override
  public float evaluer() {
    return valeur;
  }

}

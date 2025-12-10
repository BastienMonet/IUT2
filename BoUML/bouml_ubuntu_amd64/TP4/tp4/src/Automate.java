
class Automate extends Etat {


  private Etat EtatDepart;


  public Automate(Etat etatDepart) {
    EtatDepart = etatDepart;
  }

  public boolean analyseMotEx2(String mot) {
    if (mot.charAt(0) == '^' && mot.charAt(mot.length()-1) == '$'){
      mot.substring(1);
      return this.getEtatDepart().trouverMotEx2(mot);
    } else {
      return false;
    }
  }

  public boolean analyseMotEx1(String mot) {
      return this.getEtatDepart().trouverMotEx1(mot);
  }

  public boolean analyseMotEx3(String mot) {
      return this.getEtatDepart().trouverMotEx3(mot, ' ', 0);
  }

  public Etat getEtatDepart() {
    return EtatDepart;
  }

}

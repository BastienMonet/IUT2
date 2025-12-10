
class EtatFinal extends Etat {

  public EtatFinal(){
    super();
  }

  public boolean trouverMotEx2(String mot) {
    if (mot.equals("$")){
      return true;
    }else {
      return false;
    }
  }


  public boolean trouverMotEx1(String mot) {
    if (mot.equals("")){
      return true;
    }else {
      return false;
    }
  }

  public boolean trouverMotEx3(String mot) {
    return false;
  }

}

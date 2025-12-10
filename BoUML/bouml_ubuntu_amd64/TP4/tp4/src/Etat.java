import java.util.ArrayList;
import java.util.List;

class Etat {
  private List<Transition> transitions;

  public Etat() {
    transitions = new ArrayList<>();
  }

  public void ajoute(Transition t){
    transitions.add(t);
  }


  public boolean trouverMotEx2(String mot) {
    boolean res = false ;
    for (Transition t : this.transitions){
      char c = t.getSymbole();
      Etat e = t.getEtatFinal();
      boolean plus = mot.charAt(1) == '+';
      if (plus){
        if (mot.length() >= 3 && c == mot.charAt(2)){
          mot.substring(3);
          return e.trouverMotEx2(mot);
        }
        if (c == mot.charAt(0)){
          return e.trouverMotEx2(mot);
        }
      } 
      if (c == mot.charAt(0)){
        
        mot.substring(1);
        return e.trouverMotEx2(mot);
      } else {
        return false;
      }
    }
    return res;
  }


  public boolean trouverMotEx1(String mot) {
    boolean res = false ;
    for (Transition t : this.transitions){
      if (res) {
        break;
      }
      char c = t.getSymbole();
      Etat e = t.getEtatFinal();
      if (c == mot.charAt(0)){
        mot.substring(1);
        res = res || e.trouverMotEx2(mot);
        if (res == true) {
          break;
        }
      }
    }
    return res;
  }

  public boolean trouverMotEx3(String mot, char dernierSymbole, int contient) {
    boolean res = false;
    for (Transition t : this.transitions){
      char c = t.getSymbole();
      Etat e = t.getEtatFinal();
      if (contient == 0){
        if ((String.valueOf(dernierSymbole) + String.valueOf(c)).equals("GT")){
          contient++;
        }
      } else if (contient == 1){
        if ((String.valueOf(dernierSymbole) + String.valueOf(c)).equals("AG")){
          contient++;
        }
      }
      if (contient == 2) {
        return true;
      }
      mot.substring(1);
      res = res || e.trouverMotEx3(mot, c, contient);
      
      
    }
    return res;
  }

}

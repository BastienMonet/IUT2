import java.util.ArrayList;
import java.util.List;

class Client {
  private String nom;

  private List<Compte> comptes;


  public Client(String nom) {
    this.nom = nom;
    this.comptes = new ArrayList<>();
  }

  public void ajouterCompte(Compte compte){
    comptes.add(compte);
  }

  public final String getNom() {
    return nom;
  }

  public void setNom(String value) {
    nom = value;
  }

  public String to_string() {
    super.toString();
    return nom;
  }

}

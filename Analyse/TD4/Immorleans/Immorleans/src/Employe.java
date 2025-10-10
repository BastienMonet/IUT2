public class Employe {

    private String nom;
    private String prenom;
    private String email;
    private String dateRecrutement;
    

    public Employe(String nom, String prenom, String email, String dateRecrutement) {
        this.nom = nom;
        this.prenom = prenom;
        this.email = email;
        this.dateRecrutement = dateRecrutement;
    }

    public String getNom() {
        return nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public String getEmail() {
        return email;
    }

    public String getDateRecrutement() {
        return dateRecrutement;
    }
}

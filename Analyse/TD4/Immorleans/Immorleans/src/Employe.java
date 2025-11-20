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

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setDateRecrutement(String dateRecrutement) {
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

    public String toString() {
        return this.nom + " " + this.prenom;
    }
}

public class Entrepot {

    private int code;
    private String nom;
    private float departement; 

    public Entrepot(int code, String nom, float departement){
        this.code = code;
        this.nom = nom;
        this.departement = departement;
    }


    public int getCode() {
        return code;
    }


    public void setCode(int code) {
        this.code = code;
    }


    public String getNom() {
        return nom;
    }


    public void setNom(String nom) {
        this.nom = nom;
    }


    public float getDepartement() {
        return departement;
    }


    public void setDepartement(float departement) {
        this.departement = departement;
    }


    @Override
    public String toString() {
        return this.code + " " + this.nom + " " + this.departement;
    }

}
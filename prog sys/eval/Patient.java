public class Patient {

    private String nom;
    private Pathologie pathologie;



    public Patient(String nom, Pathologie pathologie) {
        this.nom = nom;
        this.pathologie = pathologie;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public Pathologie getPathologie() {
        return pathologie;
    }

    public void setPathologie(Pathologie pathologie) {
        this.pathologie = pathologie;
    }

    @Override
    public String toString() {
        return "(" + nom + "," + pathologie + ")";
    }


    
}

public class Article {

    private int reference;
    private String libelle;
    private float prix; 

    public Article(int reference, String libelle, float prix){
        this.reference = reference;
        this.libelle = libelle;
        this.prix = prix;
    }



    public int getReference() {
        return reference;
    }



    public void setReference(int reference) {
        this.reference = reference;
    }



    public String getLibelle() {
        return libelle;
    }



    public void setLibelle(String libelle) {
        this.libelle = libelle;
    }



    public float getPrix() {
        return prix;
    }



    public void setPrix(float prix) {
        this.prix = prix;
    }


    @Override
    public String toString() {
        return this.reference + " " + this.libelle + " " + this.prix;
    }

}
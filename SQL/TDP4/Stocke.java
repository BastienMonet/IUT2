public class Stocke {

    private int qte;
    private Article article;
    private Entrepot entrepot;

    public int getQte() {
        return qte;
    }

    public void setQte(int qte) {
        this.qte = qte;
    }

    public Article getArticle() {
        return article;
    }

    public void setArticle(Article article) {
        this.article = article;
    }

    public Entrepot getEntrepot() {
        return entrepot;
    }

    public void setEntrepot(Entrepot entrepot) {
        this.entrepot = entrepot;
    }

    public Stocke(int qte, Article article, Entrepot entrepot){
        this.qte = qte;
        this.article = article;
        this.entrepot = entrepot;
    }

    @Override
    public String toString() {
        return this.qte + " " + this.article + " " + this.entrepot;
    }

}
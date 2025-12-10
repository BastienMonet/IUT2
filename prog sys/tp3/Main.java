public class Main {
    public static void main(String[] args) {
        Emplacement e = new Emplacement();
        Assembleur a = new Assembleur(e);
        for (int i = 0 ; i<30 ; i++){
            Fournisseur f = new Fournisseur(e);
            f.start();
        }
        a.start();
    }
    
}

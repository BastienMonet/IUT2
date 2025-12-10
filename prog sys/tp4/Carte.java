import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Carte {
    public List<List<Integer>> matrice = new ArrayList<>(); 

    public List<List<Integer>> matriceTplus1 = new ArrayList<>(); 

    public int taille; 

    public static void main(String[] args) {
        Carte carte = new Carte(40);
        carte.affiche();
        carte.demmareFeu();

        int x = 0;

        int divise = (int)carte.taille/Runtime.getRuntime().availableProcessors();

        for (int i = 0 ; i<carte.taille ; i+= divise){
            ThreadPropagation t = new ThreadPropagation(i, i+divise - 1, carte);
            t.start();
            x = i;
        }
        if (x < carte.taille){
            ThreadPropagation t = new ThreadPropagation(x, carte.taille, carte);
            t.start();
        }


    }

    public Carte(int taille){
        Random rd = new Random();
        this.taille = taille;
        for (int i = 0 ; i<taille ; i++){
            List<Integer> ligne= new ArrayList<>(); 
            for (int j =0 ; j<taille ; j++){
                ligne.add(0);
            }
            matrice.add(ligne);
        }
         for (int i = 0 ; i<taille ; i++){
            List<Integer> ligne= new ArrayList<>(); 
            for (int j =0 ; j<taille ; j++){
                ligne.add(0);
            }
            matriceTplus1.add(ligne);
        }
    }

    public boolean fin() {
        return matrice.equals(matriceTplus1);
    }

    public int voisin(int x, int y) {
        int som = 0;
        for (int i = -1 ; i<=1 ; i++){
            for (int j = -1 ; j<=1 ; j++){
                if (i == j && i == 0) {
                    continue;
                }
                if (x+ i >= 0 && x + i < taille && y + j >= 0 && y + j < taille) {
                    som += matrice.get(x+ i).get(y + j);
                }
            }
        }
        return som;
    }

    public void propage() {
        Random rd = new Random();
        for (int i = 0 ; i<taille ; i++){
            for (int j =0 ; j<taille ; j++){
                if (matrice.get(i).get(j) == 0){
                    int total = voisin(i, j);
                    if (total >= 6) {
                        matriceTplus1.get(i).set(j, 1);
                    } else {
                        matriceTplus1.get(i).set(j, matrice.get(i).get(j));
                    }
                } else {
                    if (matrice.get(i).get(j) < 4){
                        matriceTplus1.get(i).set(j, matrice.get(i).get(j) + rd.nextInt(3));
                    } else {
                        matriceTplus1.get(i).set(j, matrice.get(i).get(j));
                    }
                }
            }
        }
        List<List<Integer>> tmp = matrice;
        matrice = matriceTplus1;
        matriceTplus1 = tmp;

    }


    public int diviseEnSousMatrice() {
        int divise = (int)this.taille/Runtime.getRuntime().availableProcessors();
        return divise;
    }

    public void demmareFeu() {
        int x= (int)this.taille/2;
        matrice.get(x).set(x, 1);
        matrice.get(x+1).set(x, 1);
        matrice.get(x).set(x+1, 1);
        matrice.get(x+1).set(x+1, 1);
    }


    public void affiche(){
        for (List<Integer> ligne : this.matrice){
            System.out.println(ligne);
        }
        System.out.println("\n\n\n\n\n");
    }
}
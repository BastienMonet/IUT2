public class ThreadPropagation extends Thread {
    
    private Carte carte; 

    private int borneMin;
    private int borenMax;

    public ThreadPropagation(int borneMin, int borneMax, Carte carte) {
        this.borneMin = borneMin;
        this.borenMax = borneMax;
        this.carte = carte;

    }

    @Override
    public void run() {
        while (! carte.fin()){
            for (int i = borneMin ; i<borenMax ; i++){
                for (int j = 0; j<carte.taille ; j++){
                    if (carte.matrice.get(i).get(j) == 0){
                        int total = carte.voisin(i, j);
                        if (total >= 6) {
                            carte.matriceTplus1.get(i).set(j, 1);
                        } else {
                                carte.matriceTplus1.get(i).set(j,  carte.matrice.get(i).get(j));
                        }
                    } else {
                        if ( carte.matrice.get(i).get(j) < 4){
                                carte.matriceTplus1.get(i).set(j,  carte.matrice.get(i).get(j)+1);
                        } else {
                                carte.matriceTplus1.get(i).set(j,  carte.matrice.get(i).get(j));
                        }
                    }
                }
            }
        }
        if (borneMin == 0){
            carte.affiche();
        }
    }
}

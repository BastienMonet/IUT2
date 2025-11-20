import java.util.List;
import java.util.ArrayList;
import java.util.Random;

class MyThread extends Thread {

    private int nb1;
    private int nb2;
    private Matrice matrice;
    private Matrice matrice2;
    private Matrice matricef;

    public MyThread(int nb1, int nb2, Matrice matrice, Matrice matrice2, Matrice matricef){
        this.nb1 = nb1;
        this.nb2 = nb2;
        this.matrice = matrice;
        this.matrice2 = matrice2;
        this.matricef = matricef;
    }

    public void run() {
        Integer res = 0;
        for (int k = 0 ; k<matrice.taille ; k++) {
            res += this.matrice.get(this.nb1, k) * matrice2.get(k, this.nb2);
        }
        matricef.set(nb1, nb2, res);
    }
}

class Matrice {

    public List<List<Integer>> matrice;
    public int taille;

    public Matrice(int taille, int nbMax){
        this.matrice = new ArrayList<>();
        this.taille = taille;


        for (int i = 0 ; i < taille ; i++) {
            List<Integer> newLigne = new ArrayList<>() ;
            for (int j = 0 ; j < taille ; j++) {
                if (nbMax > 0){
                     Random randomNumbers = new Random();
                    newLigne.add(randomNumbers.nextInt(nbMax));
                } else {
                    newLigne.add(0);
                }
               
            }
            this.matrice.add(newLigne);
        }
    }

    public Integer get(int i, int j){
        return this.matrice.get(i).get(j);
    }

    public void set(int i, int j, Integer value){
        this.matrice.get(i).set(j, value);
    }


    public void multMatirceThread(Matrice x){
        Matrice matrice0 = new Matrice(this.taille, 0);
        List<Thread> threads = new ArrayList<>();

        for (int i = 0 ; i<this.taille ; i++){
            for (int j = 0 ; j< this.taille ; j++) {
                MyThread t = new MyThread(i, j, this, x, matrice0);
                t.start();
                threads.add(t);

            }
        }
        for (Thread t : threads) {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        this.matrice = matrice0.matrice;
    }


    public void multMatirceSeq(Matrice x){
        Matrice matrice0 = new Matrice(this.taille, 0);

        for (int i = 0 ; i<this.taille ; i++){
            for (int j = 0 ; j< this.taille ; j++) {
                Integer res = 0;
                for (int k = 0 ; k<this.taille ; k++) {
                    res += this.get(i, k) * x.get(k, j);
                }
                matrice0.set(i, j, res);
            }
        }
        this.matrice = matrice0.matrice;
    }


    @Override
    public String toString() {
        String res = "";
        for (List<Integer> ligne : this.matrice) {
            res += ligne + "\n";
        }
        return res;
    }
}


public class TestThread {
    public static void main(String[] args) {
        // MyThread thread = new MyThread();
        long tmp = System.currentTimeMillis();
        int nbPrcessor = Runtime.getRuntime().availableProcessors();
        // thread.start();
        Matrice maMatrice = new Matrice(2000, 10);
        // System.out.println(maMatrice);
        maMatrice.multMatirceThread(maMatrice);
        long tmp_p_1 = System.currentTimeMillis();
        System.out.println(tmp_p_1 - tmp);
    }
}





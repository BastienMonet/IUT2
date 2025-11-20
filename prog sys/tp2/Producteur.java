import java.util.Random;

class Producteur extends Thread {

    private Donnee d;

    public Producteur(Donnee d){
        this.d=d;
    }

    @Override
    public void run() {
        Random rnd = new Random();
        for (int i = 1 ; i<1000 ; i++){
            try {
                String c =String.valueOf((char)('a' + rnd.nextInt(26)));
                d.ajouter(c);
                Thread.sleep(1000);
            } catch (InterruptedException e){
                System.err.println(e.getMessage());
            }
            

        }
        
    }
} 
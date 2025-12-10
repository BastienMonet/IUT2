import java.util.Random;

public class Assembleur extends Thread {

    Emplacement e;


    public Assembleur(Emplacement e) {
        this.e = e;

    }
    
    @Override
    public void run() {
        for (int i = 0 ; i<1000 ; i++){
            try {
                this.e.getCarosserie();
                this.e.getMoteur();
                this.e.getRoue();
                this.e.getRoue();
                this.e.getRoue();
                this.e.getRoue();
                System.out.println("la voiture a été construit");
                Thread.sleep(100);
            } catch (InterruptedException ex) {
            }
            
        }
        
    }
}
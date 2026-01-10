import java.util.Random;

public class Infirmier extends Thread {

    private Hopital hopital;

    public Infirmier(Hopital hopital){
        this.hopital = hopital;
    } 
    
    @Override
    public void run() {
        Random rd = new Random();
        for (int i = 0 ; i<1000 ; i++){
            try {
                hopital.ajouteAttente();
            } catch (Exception ex) {
                System.err.println(ex);
            }
            
        }
    }
}

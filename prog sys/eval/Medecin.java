import java.util.Random;

public class Medecin extends Thread {

    private Hopital hopital;

    public Medecin(Hopital hopital){
        this.hopital = hopital;
    } 
    
    @Override
    public void run() {
        Random rd = new Random();
        for (int i = 0 ; i<1000 ; i++){
            try {
                hopital.consulte();
                Thread.sleep(rd.nextInt(2000));
            } catch (Exception ex) {
                System.err.println(ex);
            }
            
        }
    }
}

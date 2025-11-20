public class Consomateur extends Thread {
    

    private Donnee d;

    public Consomateur(Donnee d){
        this.d=d;
    }


    @Override
    public void run(){
        for (int i = 1 ; i<1000 ; i++){
            try {
                d.retirer();
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                System.err.println(e.getMessage());

            }
            
        }

    }
}

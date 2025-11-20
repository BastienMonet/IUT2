public class Donnee {
    String data = null;

    synchronized void ajouter(String newData) throws InterruptedException{
        while (data != null){
            System.out.println("le producteur attend");
            wait();
            
        }
        data = newData;
        System.out.println("le producteur a change la donnée "+ data);
        notify();
    }

    synchronized String retirer() throws InterruptedException {
        while (data == null){
            System.out.println("le consomateur attend");
            wait();
            
        }
        System.out.println("le consomateur a consommé la donnée ");
        String tmp = data;
        data = null;
        notify();
        return tmp;
        
    }

}

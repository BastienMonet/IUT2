public class main {

    public static void main(String[] args) throws InterruptedException{
        Donnee data = new Donnee();
        Consomateur c = new Consomateur(data);
        Producteur p = new Producteur(data);
        p.start();
        c.start();
    }
    
}

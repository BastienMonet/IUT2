import java.util.Random;

public class Fournisseur extends Thread {

    Emplacement e;


    public Fournisseur(Emplacement e) {
        this.e = e;

    }
    
    @Override
    public void run() {
        Random rnd = new Random();
        Piece[] pieceArray = {Piece.CAROSSERIE, Piece.MOTEUR, Piece.ROUE};
        for (int i = 0 ; i<1000 ; i++){
            Piece piece = pieceArray[rnd.nextInt(0, 3)];
            try {
                this.e.deposer(piece);
                System.out.println("la piece " + piece + " a été construit");
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                System.err.println("lol");
            }
            
        }
        
    }
}

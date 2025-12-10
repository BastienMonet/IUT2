import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Emplacement {
    
    Lock verrouRoue = new ReentrantLock();
    Lock verrouMoteur = new ReentrantLock();
    Lock verrouCarosserie = new ReentrantLock();

    Condition fullRoue = verrouRoue.newCondition(); // une condition doit être lier a un verrou
    Condition fullMoteur = verrouMoteur.newCondition();
    Condition fullCarosserie = verrouCarosserie.newCondition();

    Condition notEmptyRoue = verrouRoue.newCondition();
    Condition notEmptyMoteur =verrouMoteur.newCondition();
    Condition notEmptyCarosserie = verrouCarosserie.newCondition();


    List<Piece> stock = new ArrayList<>();

    public void deposer(Piece piece) throws InterruptedException{
        switch (piece) {
            case Piece.MOTEUR :
                verrouMoteur.lock();
                while (nbMoteur() == 5){
                    fullMoteur.await();
                }
                stock.add(piece);
                notEmptyMoteur.signal();

                verrouMoteur.unlock();
                break;
            case Piece.CAROSSERIE :
                verrouCarosserie.lock();
                while (nbCarorerie() == 3){
                    fullCarosserie.await();
                }
                stock.add(piece);
                notEmptyCarosserie.signal();
                verrouCarosserie.unlock();
                break;
            case Piece.ROUE : 
                verrouRoue.lock();
                while (nbRoues() == 20){
                    fullRoue.await();
                }
                stock.add(piece);
                notEmptyRoue.signal();

                verrouRoue.unlock();
                break;
        }
    }

    public void getRoue() throws InterruptedException{
        verrouRoue.lock();
        while (nbRoues() < 4){
            notEmptyRoue.await();
        }
        stock.remove(Piece.ROUE);
        fullRoue.signal();
        verrouRoue.unlock();
    }

    public void getCarosserie() throws InterruptedException{
        verrouCarosserie.lock();
        while (nbCarorerie() < 1){
            notEmptyCarosserie.await();
        }
        stock.remove(Piece.ROUE);
        fullCarosserie.signal();
        verrouCarosserie.unlock();
    }


    public void getMoteur() throws InterruptedException{
        verrouMoteur.lock();
        while (nbMoteur() < 1){
            notEmptyMoteur.await();
        }
        stock.remove(Piece.ROUE);
        fullMoteur.signal();
        verrouMoteur.unlock();
    }



    public int nbRoues(){
        int cpt = 0;
        for (Piece p : this.stock){
            if (p == Piece.ROUE) {
                cpt ++;
            }
        }
        return cpt;
    }


    public int nbCarorerie(){
        int cpt = 0;
        for (Piece p : this.stock){
            if (p == Piece.CAROSSERIE) {
                cpt ++;
            }
        }
        return cpt;
    }


    public int nbMoteur(){
        int cpt = 0;
        for (Piece p : this.stock){
            if (p == Piece.MOTEUR) {
                cpt ++;
            }
        }
        return cpt;
    }

}

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import java.util.Random;
public class CentreTraumato extends Hopital {

    Lock verrouTraumaAttente = new ReentrantLock();

    Condition TraumaAttenteFull = verrouTraumaAttente.newCondition();
    Condition TraumaAttenteEmpty = verrouTraumaAttente.newCondition();

    private List<Patient> attenteTrauma;

    private Random rd;

    public CentreTraumato(){
        super();
        this.rd =  new Random();
        attenteTrauma = new ArrayList<>(taillAttente);
    }

    @Override
    public void ajouteAttente() throws InterruptedException{
        try {
            verrouTraumaAttente.lock();
            if (getPatientT() == null){
                return;
            }
            while (attenteTrauma.size() == taillAttente){
                System.out.println("la file est pleine");
                TraumaAttenteFull.await();
            }
            Thread.sleep(rd.nextInt(2000));
            System.out.println("patient ajouté");
            TraumaAttenteEmpty.signal();
            Patient patient =  getPatientT();
            Hopital.removePatient(patient);
            attenteTrauma.add(patient);

        } finally {
            verrouTraumaAttente.unlock();
        }
    }

    @Override
    public void consulte() throws InterruptedException{
        try {
            verrouTraumaAttente.lock();
            if (this.getPatientT() == null){
                return;
            }
            while (attenteTrauma.size() == 0){
                System.out.println("plus personne dans la file d'attente");
                TraumaAttenteEmpty.await();
            }
            TraumaAttenteFull.signal();
            attenteTrauma.remove(this.getPatientT());
            System.out.println("patient retirer du centre traumato");

        } finally {
            verrouTraumaAttente.unlock();
        }
    }

    public Patient getPatientT(){
        for (Patient p : getPatient()){
            if (p.getPathologie() == Pathologie.TRAUMA){
                return p;
            }
        }
        return null;
    }



    
    

}

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public abstract class Hopital {

    protected static List<Patient> patients = new ArrayList<>();

    protected static int taillAttente = 2;


    public Hopital() {
    }
 

    public abstract void ajouteAttente() throws Exception;

    public abstract void consulte() throws Exception;
    
    public static List<Patient> getPatient(){
        return patients;
    }


    public static void setPatient(List<Patient> list_patients){
        Hopital.patients = new ArrayList<>(list_patients);
    }

    public static void removePatient(Patient patients){
        Hopital.patients.remove(patients);
    }

    public static void setTailleAttente(int taillAttente){
        Hopital.taillAttente = taillAttente;
    }

}
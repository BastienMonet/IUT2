import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Hopital.setTailleAttente(4);
        CentreTraumato ct = new CentreTraumato();
        Hopital.setPatient(Arrays.asList(new Patient("bob", Pathologie.TRAUMA)));
        Infirmier infTraumato = new Infirmier(ct);
        Medecin medTraumato = new Medecin(ct);
        infTraumato.start();
        medTraumato.start();

    }
    
}

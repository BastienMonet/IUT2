import java.util.ArrayList;
import java.util.List;

public class Recrutement {

    private List<Employe> employes;
    private int index;

    public Recrutement() {
        employes = new ArrayList<>();
        index = -1;
    }

    public void add(Employe e) {
        employes.add(e);
    }

    public void removeEmploye(int i) {
        if (i >= 0 && i < employes.size()) {
            employes.remove(i);
        }
    }

    public void ajouterEmploye(Employe employe) {
        employes.add(employe);
    }

    public List<Employe> getEmployes() {
        return employes;
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int new_index){
        this.index = new_index;
    }

    public Employe getEmployeCourant() {
        if (index >= 0 && index < employes.size()) {
            return employes.get(index);
        }
        return null;
    }

}

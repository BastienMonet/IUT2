import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Repertoire extends ArrayList<Employe>{

    private int index;

    public Repertoire(String nomFichier) {
        super();
        this.clear();
        index = 0;
        chargerRepertoire(nomFichier);
    }

    public void sauvegarderRepertoire(String nomFichier){
        String res = "Nom,Prénom,Email,DateRecrutement\n";
        try  (BufferedWriter writer = new BufferedWriter(new FileWriter(nomFichier))) {
            for (Employe employe : this){
                res += employe.getNom() + "," + employe.getPrenom() + "," + employe.getEmail() + "," + employe.getDateRecrutement() + "\n";
            }
            writer.write(res);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        } 

    }

    public void chargerRepertoire(String nomFichier){
        this.clear();
        String ligne;
        try (BufferedReader br = new BufferedReader(new FileReader(nomFichier))) {
            br.readLine();
            while ((ligne = br.readLine()) != null) {
                List<String> valeurs = List.of(ligne.split(","));
                Employe emp= new Employe(valeurs.get(0), valeurs.get(1), valeurs.get(2), valeurs.get(3));
                this.add(emp);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(this);
    }

    public void init(){
        index = 0;
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int new_index){
        this.index = new_index;
    }

    public Employe getEmployeCourant() {
        if (index >= 0 && index < this.size()) {
            return this.get(index);
        }
        return null;
    }

}

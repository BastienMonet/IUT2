
import java.util.*;
public class Compte {
  private float solde;

  private String numero;

  private float decouvertAutorise =   100;

  private List<Operation> operations;

  /**
   *  constructeur    
   */
  public Compte(String numero, float solde) {
      this.operations = new ArrayList<>();
      this.numero=numero;
      this.solde=solde;
  }

  /**
   *  getters/setters
   */
  public void setSolde(float val) {
        this.solde = val;
  }

  public float getSolde() {
        return this.solde;
  }

  public void setNumero(String num) {
        this.numero = num;
  }

  public String getNumero() {
        return this.numero;
  }

  public void setDecouvertAutorise(float val) {
        this.decouvertAutorise = val;
  }

  public float getDecouvertAutorise() {
        return this.decouvertAutorise;
  }

  /**
   *  opérations métiers
   */
  public boolean debiter(float montant, String info) {
        if(montant>0){
            float res = this.solde-montant;
            if(res>=this.decouvertAutorise){ // vérification solde après opératioin
                this.solde = res;
                Operation op = new Operation(new Date(), -1 * solde);
                ajouterOperation(op);
                return true;
            }
        }
        return false;
  }

  public boolean crediter(float montant, String info) {
        if(montant>0){
            this.solde += montant;
            Operation op = new Operation(new Date(), solde);
            ajouterOperation(op);
            return true;
        }
        return false;
  }

  public String toString() {
        return "je suis le compte bancaire numero " + numero + "avec le solde " + solde;
  }

  public List<Operation> getHistorique() {
      return operations;
  }

  public void ajouterOperation(Operation op) {
     operations.add(op);
  }

}

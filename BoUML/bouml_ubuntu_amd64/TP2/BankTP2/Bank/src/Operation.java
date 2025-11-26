
import java.util.*;
public class Operation {
  private Date date;

  private float montant;

  public Operation(Date date, float montant) {
  }

  public final Date getDate() {
    return date;
  }

  public void setDate(Date value) {
    date = value;
  }

  public final float getMontant() {
    return montant;
  }

  public void setMontant(float value) {
    montant = value;
  }

  @Override
  public String toString(){
    return date + " " + montant;
  }

}

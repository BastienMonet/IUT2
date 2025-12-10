import java.util.ArrayList;
import java.util.List;

abstract class Observable {

  private List<IObservateur> observateurs = new ArrayList<>();

  public void addObservateur(IObservateur obs) {
    this.observateurs.add(obs);
  }

  public void notiferObs(String message) {
    for (IObservateur observateur : this.observateurs) {
      observateur.notification(message);
    }
  }

}

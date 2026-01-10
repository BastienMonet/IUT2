import java.util.ArrayList;
import java.util.List;

class Addition extends Operation {
  private List<Operation> operations;

  public Addition() {
    super();
    operations = new ArrayList<>();

  }

  public void addOperation(Operation o) {
    operations.add(o);
  }

  @Override
  public float evaluer() {
    float som = 0;
    for (Operation o : operations){
      som += o.evaluer();
    }
    return som;
  }

}

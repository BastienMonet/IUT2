import java.util.List;
import java.util.concurrent.RecursiveTask;

public class Max extends RecursiveTask<Integer>{

    private List<Integer> listint;
    private int max;

    private int borneInf;
    private int borneSup;

    public Max(int borneInf, int borneSup, List<Integer> listint){
        this.borneInf = borneInf;
        this.borneSup = borneSup;
        this.listint = listint;
    }
    

    @Override
    protected Integer compute() {
        if (borneSup - borneInf < 100){
            max = 0;
            for (int i = borneInf ; i<borneSup ; i++){
                if (listint.get(i) > max){
                    max = listint.get(i);
                }
            }
            return max;
        } else {
            int borneInter = (int) borneInf + (borneSup - borneInf) / 2;
            Max left = new Max(borneInf, borneInter, listint);
            left.fork();
            Max right = new Max(borneInter, borneSup, listint);
            return Math.max(right.compute(), left.join());
        }
        
    }
    
}

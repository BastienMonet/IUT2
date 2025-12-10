import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ForkJoinPool;

public class Main {

    public static void main(String[] args) {
        ForkJoinPool pool = new ForkJoinPool();
        List<Integer> l = Arrays.asList(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10);
        pool.invoke(new Max(0, l.size(), l));
    }
    
}

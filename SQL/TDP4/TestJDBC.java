

public class TestJDBC {
    public static void main (String[] args){
        ConnexionMySQL co = new ConnexionMySQL("servinfo-maria", "DBmonet", "monet", "monet");
        EntrepotBD test = new EntrepotBD(co);
        try {
            System.out.println(test.maxReference());
            System.out.println(test.listArticle());
            // test.entrepotParDepartement();
            test.lesEntrepotsPossedeArticle(1);



        } catch (Exception e){
            System.out.println(e);
        }
    }
}



class main {
    public static void main(String[] args) {
        Nombre n1 = new Nombre(1);
        Nombre n2 = new Nombre(2);
        Addition a1 = new Addition();
        a1.addOperation(n1);    
        a1.addOperation(n2);
        System.out.println(a1.evaluer()); 
    }
}

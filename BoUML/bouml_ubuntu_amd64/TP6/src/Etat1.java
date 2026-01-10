
class Etat1 implements IEtat {

    @Override
    public void event1(Automate a) {
        a.setEtatCourant(new Etat2());
        System.out.println("je passe a l'event 2");
        a.getControle().action1();
    }

    @Override
    public void event2(Automate a) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'event2'");
    }
}

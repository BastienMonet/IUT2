
class Etat2 implements IEtat {

    @Override
    public void event1(Automate a) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'event1'");
    }

    @Override
    public void event2(Automate a) {
        a.setEtatCourant(new Etat1());
        System.out.println("je passe a l'event 1");
        a.getControle().action2();

    }
}

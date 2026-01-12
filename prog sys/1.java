import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class StockConcurrent {
    // Shared quantities [cite: 7]
    private int carrosseries = 0, moteurs = 0, roues = 0;
    
    // Independent locks for each part type to allow concurrent delivery [cite: 12]
    private final Lock lockC = new ReentrantLock();
    private final Lock lockM = new ReentrantLock();
    private final Lock lockR = new ReentrantLock();

    // Conditions for full stock [cite: 11]
    private final Condition fullC = lockC.newCondition();
    private final Condition fullM = lockM.newCondition();
    private final Condition fullR = lockR.newCondition();

    // The assembler needs to check all three, so we can use a separate 
    // mechanism or logic to notify the assembler.
    private final Lock lockAssembler = new ReentrantLock();
    private final Condition partsReady = lockAssembler.newCondition();

    public void ajouterCarrosserie() throws InterruptedException {
        lockC.lock();
        try {
            while (carrosseries >= 3) fullC.await(); // [cite: 7, 11]
            carrosseries++;
            signalAssembler(); // Notify that a part arrived
        } finally { lockC.unlock(); }
    }

    public void ajouterMoteur() throws InterruptedException {
        lockM.lock();
        try {
            while (moteurs >= 5) fullM.await(); // [cite: 7, 11]
            moteurs++;
            signalAssembler();
        } finally { lockM.unlock(); }
    }

    public void ajouterRoue() throws InterruptedException {
        lockR.lock();
        try {
            while (roues >= 20) fullR.await(); // [cite: 7, 11]
            roues++;
            signalAssembler();
        } finally { lockR.unlock(); }
    }

    private void signalAssembler() {
        lockAssembler.lock();
        try { partsReady.signal(); } 
        finally { lockAssembler.unlock(); }
    }

    public void assemblerVoiture() throws InterruptedException {
        while (true) {
            lockAssembler.lock();
            try {
                // The assembler must lock ALL part locks to check consistency
                lockC.lock(); lockM.lock(); lockR.lock();
                try {
                    if (carrosseries >= 1 && moteurs >= 1 && roues >= 4) {
                        carrosseries--;
                        moteurs--;
                        roues -= 4;
                        fullC.signal();
                        fullM.signal();
                        fullR.signalAll();
                        System.out.println("Voiture assemblée !");
                        return; // Exit the method after successful assembly
                    }
                } finally {
                    lockR.unlock(); lockM.unlock(); lockC.unlock();
                }
                // If parts weren't ready, wait for a signal [cite: 10]
                partsReady.await();
            } finally {
                lockAssembler.unlock();
            }
        }
    }
}
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class ConstructionAutomobile {

    // --- INNER CLASS: Logic for each specific part ---
    static class PartStock {
        private final String name;
        private final int capacity;
        private int count = 0;
        private final Lock lock = new ReentrantLock();
        private final Condition isFull = lock.newCondition();
        private final Condition hasParts = lock.newCondition();

        public PartStock(String name, int capacity) {
            this.name = name;
            this.capacity = capacity;
        }

        public void deposit(int amount) throws InterruptedException {
            lock.lock();
            try {
                while (count + amount > capacity) {
                    System.out.println("[STOCK FULL] Supplier waiting for " + name);
                    isFull.await(); // [cite: 11, 12]
                }
                count += amount;
                System.out.println("Added " + name + " | Total: " + count + "/" + capacity);
                hasParts.signalAll(); // 
            } finally {
                lock.unlock();
            }
        }

        public void withdraw(int amount) throws InterruptedException {
            lock.lock();
            try {
                while (count < amount) {
                    System.out.println("[PARTS MISSING] Assembler waiting for " + name);
                    hasParts.await(); // [cite: 10, 12]
                }
                count -= amount;
                isFull.signalAll(); // 
            } finally {
                lock.unlock();
            }
        }
    }

    // --- INNER CLASS: The Factory (Stock Management) ---
    static class Factory {
        // Separate instances ensure concurrent access for different parts 
        private final PartStock chassis = new PartStock("Carrosserie", 3);
        private final PartStock engines = new PartStock("Moteur", 5);
        private final PartStock wheels = new PartStock("Roues", 20);
        private final PartStock electronics = new PartStock("Electronique", 10);

        public void supplyBody() throws InterruptedException { chassis.deposit(1); }
        public void supplyEngine() throws InterruptedException { engines.deposit(1); }
        public void supplyWheels() throws InterruptedException { wheels.deposit(1); }
        public void supplyElectronics() throws InterruptedException { electronics.deposit(1); }

        public void assemble() throws InterruptedException {
            // Assembler retrieves components individually [cite: 8, 9]
            chassis.withdraw(1);
            engines.withdraw(1);
            wheels.withdraw(4);
            electronics.withdraw(1);
            System.out.println(">>> SUCCESS: A car has been fully assembled!");
        }
    }

    // --- MAIN: Thread Management ---
    public static void main(String[] args) {
        Factory factory = new Factory();

        // Supplier Threads 
        Thread bodySupplier = new Thread(() -> {
            try { while(true) { factory.supplyBody(); Thread.sleep(1000); } } 
            catch (InterruptedException e) { }
        });

        Thread engineSupplier = new Thread(() -> {
            try { while(true) { factory.supplyEngine(); Thread.sleep(1200); } } 
            catch (InterruptedException e) { }
        });

        Thread wheelSupplier = new Thread(() -> {
            try { while(true) { factory.supplyWheels(); Thread.sleep(300); } } 
            catch (InterruptedException e) { }
        });

        Thread electronicSupplier = new Thread(() -> {
            try { while(true) { factory.supplyElectronics(); Thread.sleep(1500); } } 
            catch (InterruptedException e) { }
        });

        // Assembler Thread 
        Thread assembler = new Thread(() -> {
            try { while(true) { factory.assemble(); Thread.sleep(2000); } } 
            catch (InterruptedException e) { }
        });

        // Start all processes in parallel [cite: 6]
        bodySupplier.start();
        engineSupplier.start();
        wheelSupplier.start();
        electronicSupplier.start();
        assembler.start();
    }
} 


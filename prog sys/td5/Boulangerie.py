from threading import Lock, Condition,Thread
import Pain
import Random

class Boulangerie :

    def __init__(self, taille):
        self.taille = taille
        self.list_pain : list[Pain] = [] 
        self.lock = Lock()
        self.full = Condition(self.lock)
        self.empty = Condition(self.lock)

    def produire(self, pain : Pain):
        with self.lock:
            while(len(self.list_pain) == self.taille):
                self.full.wait()
            self.list_pain.append(pain)
            self.empty.notify()


    def consomer(self):
        with self.lock:
            while(len(self.list_pain) == 0):
                self.empty.wait()
            self.list_pain.pop()
            self.full.notify()

class Boulanger(Thread) :

    def __init__(self, donne):
        self.donne = donne
        self.type_baguette = ["tradition", "campagne", "complet", "seigle"]

    def run(self):
        for _ in range(100):
            self.produire(Pain(Random.randint(0, 100), self.type_baguette[Random.randint(0,3)]))
            Thread.sleep(0.5)

class Client(Thread) :

    def __init__(self, donne : Boulangerie):
        self.donne = donne

    def run(self):
        for _ in range(100):
            self.donne.consomer()
            Thread.sleep(0.5)




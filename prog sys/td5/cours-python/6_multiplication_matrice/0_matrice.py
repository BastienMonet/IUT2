import threading
import random
import time
import sys
import os

class Thr(threading.Thread):
    """
    Équivalent de Thr.java : Chaque thread calcule une case (i, j)
    """
    def __init__(self, m1, m2, res, i, j):
        super().__init__()
        self.i = i
        self.j = j
        self.m1 = m1
        self.m2 = m2
        self.res = res

    def run(self):
        n = self.m1.size()
        val = 0
        for k in range(n):
            val += self.m1.get(self.i, k) * self.m2.get(k, self.j)
        self.res.set(self.i, self.j, val)


class ThrL(threading.Thread):
    """
    Chaque thread calcule une ligne i
    """
    def __init__(self, m1, m2, res, i):
        super().__init__()
        self.i = i
        self.m1 = m1
        self.m2 = m2
        self.res = res

    def run(self):
        n = self.m1.size()
        for j in range(n):
            val = 0
            for k in range(n):
                val += self.m1.get(self.i, k) * self.m2.get(k, j)
            self.res.set(self.i, j, val)


class ThrC(threading.Thread):
    """
    Chaque thread calcule une plage de lignes [debut, fin[
    """
    def __init__(self, m1, m2, res, debut, fin):
        super().__init__()
        self.debut = debut
        self.fin = fin
        self.m1 = m1
        self.m2 = m2
        self.res = res

    def run(self):
        n = self.m1.size()
        for i in range(self.debut, self.fin):
            for j in range(n):
                val = 0
                for k in range(n):
                    val += self.m1.get(i, k) * self.m2.get(k, j)
                self.res.set(i, j, val)


# --- Classe Matrice ---

class Matrice:
    def __init__(self, n, max_val=None):
        self.mat = []
        # Initialisation vide (zéros)
        if max_val is None:
            for i in range(n):
                row = [0] * n
                self.mat.append(row)
        # Initialisation aléatoire
        else:
            for i in range(n):
                row = [random.randrange(max_val) for _ in range(n)]
                self.mat.append(row)

    def size(self):
        return len(self.mat)

    def get(self, i, j):
        return self.mat[i][j]

    def set(self, i, j, val):
        self.mat[i][j] = val

    def multiplication_seq(self, matrice):
        """ Version séquentielle """
        if matrice.size() == self.size():
            n = self.size()
            res = Matrice(n)
            for i in range(n):
                for j in range(n):
                    val = 0
                    for k in range(n):
                        val += self.get(i, k) * matrice.get(k, j)
                    res.set(i, j, val)
            return res
        raise ValueError("Matrice taille différente")

    def multiplication_par(self, matrice):
        """ Version parallèle : un thread par case (Attention: très lent) """
        if matrice.size() == self.size():
            n = self.size()
            res = Matrice(n)
            list_threads = []
            
            for i in range(n):
                for j in range(n):
                    thr = Thr(self, matrice, res, i, j)
                    list_threads.append(thr)
                    thr.start()
            
            for thr in list_threads:
                thr.join()
            
            return res
        raise ValueError("Matrice taille différente")

    def multiplication_par_ligne(self, matrice):
        """ Version parallèle : un thread par ligne """
        if matrice.size() == self.size():
            n = self.size()
            res = Matrice(n)
            list_threads = []

            for i in range(n):
                thr_l = ThrL(self, matrice, res, i)
                list_threads.append(thr_l)
                thr_l.start()

            for thr_l in list_threads:
                thr_l.join()
            
            return res
        raise ValueError("Matrice taille différente")

    def multiplication_par_coeur(self, matrice):
        """ Version parallèle : découpage par cœurs CPU """
        if matrice.size() == self.size():
            n = self.size()
            res = Matrice(n)
            list_threads = []
            
            # Nombre de processeurs logiques
            nb_threads = os.cpu_count() or 4 # Fallback à 4 si os.cpu_count échoue
            if nb_threads > n: 
                nb_threads = n
                
            nb_lignes_par_thread = n // nb_threads

            for i in range(nb_threads):
                debut = i * nb_lignes_par_thread
                fin = (i + 1) * nb_lignes_par_thread
                # Le dernier thread prend le reste
                if i == nb_threads - 1:
                    fin = n
                
                thr_c = ThrC(self, matrice, res, debut, fin)
                list_threads.append(thr_c)
                thr_c.start()

            for thr_c in list_threads:
                thr_c.join()

            return res
        raise ValueError("Matrice taille différente")

    def __str__(self):
        n = self.size()
        res_str = ""
        for i in range(n):
            row_str = "\t".join(str(self.get(i, j)) for j in range(n))
            res_str += row_str + "\n"
        return res_str

# --- Main ---

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python matrice.py <tailleMatrice> <typeAlgo>")
        print("typeAlgo : seq | ligne | case | coeur (default)")
    else:
        taille = int(sys.argv[1])
        mat1 = Matrice(taille, 10)
        mat2 = Matrice(taille, 10)
        
        algo = "coeur"
        if len(sys.argv) > 2:
            algo = sys.argv[2]

        start_time = time.time()
        
        if algo == "seq":
            res = mat1.multiplication_seq(mat2)
        elif algo == "ligne":
            res = mat1.multiplication_par_ligne(mat2)
        elif algo == "case":
            res = mat1.multiplication_par(mat2)
        elif algo == "coeur":
            res = mat1.multiplication_par_coeur(mat2)
        else:
            res = mat1.multiplication_par_coeur(mat2)

        end_time = time.time()
        
        # print(mat1)
        # print(mat2)
        # print(res)
        
        duration_ms = (end_time - start_time) * 1000
        print(f"{duration_ms:.2f} ms")


# temps execution
#       50      500     1000
# seq   31ms    14s     2min
# case  300ms   53s     6min
# ligne 53ms    19s     3min
# coeur 42ms    17s     2min
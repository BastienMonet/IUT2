# =============================
# FICHIER DE RÉVISION : NUMPY
# =============================

# NumPy est une bibliothèque Python pour le calcul numérique.
# Elle permet de manipuler efficacement des tableaux multidimensionnels (ndarray).

# 1. IMPORTATION
import numpy as np

# 2. CRÉER DES TABLEAUX

# Tableau à partir d'une liste
a = np.array([1, 2, 3])
print("Tableau 1D :", a)

# Tableau 2D
b = np.array([[1, 2, 3], [4, 5, 6]])
print("Tableau 2D :\n", b)

# Tableaux spéciaux
zeros = np.zeros((2, 3))      # tableau rempli de zéros
ones = np.ones((2, 2))        # tableau rempli de uns
full = np.full((2, 2), 7)     # tableau rempli d'une valeur (ici 7)
identity = np.eye(3)          # matrice identité 3x3
arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)  # 5 valeurs entre 0 et 1 inclus

print("Zéros :\n", zeros)
print("Uns :\n", ones)
print("Full :\n", full)
print("Identité :\n", identity)
print("Arange :", arange)
print("Linspace :", linspace)

# 3. ATTRIBUTS D'UN TABLEAU
print("\n--- Attributs ---")
print("Forme (shape) :", b.shape)       # dimensions
print("Nombre de dimensions (ndim) :", b.ndim)
print("Nombre total d'éléments (size) :", b.size)
print("Type des éléments (dtype) :", b.dtype)

# 4. OPÉRATIONS DE BASE
c = np.array([1, 2, 3])
d = np.array([4, 5, 6])

print("\n--- Opérations élément par élément ---")
print("Addition :", c + d)
print("Multiplication :", c * d)
print("Puissance :", c ** 2)
print("Sinus :", np.sin(c))

# Opérations globales
print("Somme :", np.sum(c))
print("Moyenne :", np.mean(c))
print("Écart-type :", np.std(c))
print("Minimum :", np.min(c))
print("Maximum :", np.max(c))

# 5. INDEXATION ET TRANCHE (SLICING)
e = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("\n--- Indexation ---")
print("Élément [1,2] :", e[1, 2])        # 7
print("Première ligne :", e[0, :])        # [1 2 3 4]
print("Deuxième colonne :", e[:, 1])      # [2 6 10]
print("Sous-tableau :", e[0:2, 1:3])      # [[2 3], [6 7]]

# 6. MANIPULATION DE FORME
f = np.array([1, 2, 3, 4, 5, 6])
reshaped = f.reshape((2, 3))
print("\n--- Reshape ---")
print("Original :", f)
print("Reshapé :\n", reshaped)

# Transposition
print("Transposé :\n", reshaped.T)

# Aplatir
flattened = reshaped.flatten()
print("Aplatit :", flattened)

# 7. CONDITIONS ET FILTRAGE
g = np.array([1, 5, 3, 8, 2])
print("\n--- Conditions ---")
print("Éléments > 3 :", g[g > 3])         # [5 8]
print("Indices où condition vraie :", np.where(g > 3))

# 8. ALGÈBRE LINÉAIRE
h = np.array([[1, 2], [3, 4]])
i = np.array([[5, 6], [7, 8]])

print("\n--- Algèbre linéaire ---")
print("Produit matriciel :\n", np.dot(h, i))
print("Déterminant :", np.linalg.det(h))
print("Inverse :\n", np.linalg.inv(h))
print("Valeurs propres :", np.linalg.eigvals(h))

# 9. FONCTIONS UTILES
j = np.random.rand(3, 3)  # nombres aléatoires entre 0 et 1
k = np.random.randint(0, 10, size=(2, 4))  # entiers aléatoires

print("\n--- Nombres aléatoires ---")
print("Random (0-1) :\n", j)
print("Random int (0-9) :\n", k)

# 10. COPIE VS VUE
original = np.array([1, 2, 3])
copie = original.copy()    # copie indépendante
vue = original             # même données en mémoire

vue[0] = 99
print("\n--- Copie vs Vue ---")
print("Original après modification de vue :", original)  # [99, 2, 3]
print("Copie inchangée :", copie)                        # [1, 2, 3]

# =============================
# FIN DU FICHIER DE RÉVISION
# =============================
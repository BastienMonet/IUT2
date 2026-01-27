/**
 * Fichier de révision en langage C (~500 lignes)
 * Auteur : Révision C
 * Date : 20 janvier 2026
 * Objectif : Réviser les bases du C
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Définitions constantes
#define TAILLE_TAB 10
#define MAX_NOM 50

// Structure pour représenter une personne
typedef struct {
    char nom[MAX_NOM];
    int age;
} Personne;

// === PROTOTYPES DE FONCTIONS ===
void afficherMessage(void);
int somme(int a, int b);
void echange(int *a, int *b);
void remplirTableau(int tab[], int taille);
void afficherTableau(const int tab[], int taille);
int rechercheLineaire(const int tab[], int taille, int val);
void triBulles(int tab[], int taille);
void manipulerChaine(char ch[]);
Personne creerPersonne(const char *nom, int age);
void afficherPersonne(const Personne *p);
void sauvegarderPersonneFichier(const Personne *p, const char *nomFichier);
Personne *lirePersonneFichier(const char *nomFichier);
int *creerTableauDynamique(int taille);
void libererTableauDynamique(int *tab);

// === FONCTION PRINCIPALE ===
int main(void) {
    printf("=== REVISION LANGAGE C ===\n\n");

    // 1. Appel simple de fonction
    afficherMessage();

    // 2. Opérations arithmétiques
    int x = 5, y = 3;
    printf("Somme de %d et %d = %d\n", x, y, somme(x, y));

    // 3. Échange via pointeurs
    printf("\nAvant échange : x = %d, y = %d\n", x, y);
    echange(&x, &y);
    printf("Après échange : x = %d, y = %d\n", x, y);

    // 4. Tableau statique
    int tableau[TAILLE_TAB];
    remplirTableau(tableau, TAILLE_TAB);
    printf("\nTableau initial : ");
    afficherTableau(tableau, TAILLE_TAB);

    // 5. Recherche linéaire
    int valRech = 7;
    int pos = rechercheLineaire(tableau, TAILLE_TAB, valRech);
    if (pos != -1) {
        printf("Valeur %d trouvée à l'indice %d\n", valRech, pos);
    } else {
        printf("Valeur %d non trouvée\n", valRech);
    }

    // 6. Tri à bulles
    triBulles(tableau, TAILLE_TAB);
    printf("Tableau trié : ");
    afficherTableau(tableau, TAILLE_TAB);

    // 7. Manipulation de chaînes
    char texte[] = "Bonjour le monde!";
    printf("\nChaîne originale : %s\n", texte);
    manipulerChaine(texte);
    printf("Chaîne modifiée : %s\n", texte);

    // 8. Utilisation de structures
    Personne p1 = creerPersonne("Alice", 28);
    afficherPersonne(&p1);

    // 9. Sauvegarde dans un fichier
    sauvegarderPersonneFichier(&p1, "personne.txt");
    printf("Données sauvegardées dans 'personne.txt'\n");

    // 10. Lecture depuis un fichier
    Personne *p2 = lirePersonneFichier("personne.txt");
    if (p2 != NULL) {
        printf("Lecture depuis fichier : ");
        afficherPersonne(p2);
        free(p2); // libérer la mémoire allouée dynamiquement
    }

    // 11. Allocation dynamique
    int tailleDyn = 5;
    int *tabDyn = creerTableauDynamique(tailleDyn);
    if (tabDyn == NULL) {
        fprintf(stderr, "Erreur d'allocation mémoire\n");
        return EXIT_FAILURE;
    }
    for (int i = 0; i < tailleDyn; i++) {
        tabDyn[i] = i * i;
    }
    printf("\nTableau dynamique : ");
    for (int i = 0; i < tailleDyn; i++) {
        printf("%d ", tabDyn[i]);
    }
    printf("\n");
    libererTableauDynamique(tabDyn);

    // 12. Boucle while + switch
    printf("\nMenu interactif (simulé) :\n");
    int choix = 2;
    switch (choix) {
        case 1:
            printf("Option 1 sélectionnée.\n");
            break;
        case 2:
            printf("Option 2 sélectionnée (exemple).\n");
            break;
        default:
            printf("Option invalide.\n");
    }

    // 13. Génération aléatoire (bonus)
    srand(time(NULL));
    printf("\nNombre aléatoire entre 1 et 100 : %d\n", rand() % 100 + 1);

    printf("\n=== FIN DE LA RÉVISION ===\n");
    return EXIT_SUCCESS;
}

// === DÉFINITIONS DES FONCTIONS ===

void afficherMessage(void) {
    printf("Bienvenue dans ce programme de révision en C !\n");
}

int somme(int a, int b) {
    return a + b;
}

void echange(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void remplirTableau(int tab[], int taille) {
    srand(42); // graine fixe pour reproductibilité
    for (int i = 0; i < taille; i++) {
        tab[i] = rand() % 10 + 1; // valeurs entre 1 et 10
    }
}

void afficherTableau(const int tab[], int taille) {
    for (int i = 0; i < taille; i++) {
        printf("%d ", tab[i]);
    }
    printf("\n");
}

int rechercheLineaire(const int tab[], int taille, int val) {
    for (int i = 0; i < taille; i++) {
        if (tab[i] == val) {
            return i;
        }
    }
    return -1; // non trouvé
}

void triBulles(int tab[], int taille) {
    for (int i = 0; i < taille - 1; i++) {
        for (int j = 0; j < taille - i - 1; j++) {
            if (tab[j] > tab[j + 1]) {
                echange(&tab[j], &tab[j + 1]);
            }
        }
    }
}

void manipulerChaine(char ch[]) {
    // Met tout en majuscules
    for (int i = 0; ch[i] != '\0'; i++) {
        if (ch[i] >= 'a' && ch[i] <= 'z') {
            ch[i] = ch[i] - 'a' + 'A';
        }
    }
}

Personne creerPersonne(const char *nom, int age) {
    Personne p;
    strncpy(p.nom, nom, MAX_NOM - 1);
    p.nom[MAX_NOM - 1] = '\0'; // sécurité
    p.age = age;
    return p;
}

void afficherPersonne(const Personne *p) {
    printf("Nom : %s, Âge : %d ans\n", p->nom, p->age);
}

void sauvegarderPersonneFichier(const Personne *p, const char *nomFichier) {
    FILE *f = fopen(nomFichier, "w");
    if (f == NULL) {
        perror("Erreur d'ouverture du fichier en écriture");
        return;
    }
    fprintf(f, "%s\n%d\n", p->nom, p->age);
    fclose(f);
}

Personne *lirePersonneFichier(const char *nomFichier) {
    FILE *f = fopen(nomFichier, "r");
    if (f == NULL) {
        perror("Erreur d'ouverture du fichier en lecture");
        return NULL;
    }
    Personne *p = malloc(sizeof(Personne));
    if (p == NULL) {
        fclose(f);
        return NULL;
    }
    if (fgets(p->nom, MAX_NOM, f) == NULL) {
        free(p);
        fclose(f);
        return NULL;
    }
    // Supprimer le \n de fgets si présent
    p->nom[strcspn(p->nom, "\n")] = '\0';
    if (fscanf(f, "%d", &(p->age)) != 1) {
        free(p);
        fclose(f);
        return NULL;
    }
    fclose(f);
    return p;
}

int *creerTableauDynamique(int taille) {
    int *tab = malloc(taille * sizeof(int));
    if (tab == NULL) {
        return NULL;
    }
    // Initialisation optionnelle
    for (int i = 0; i < taille; i++) {
        tab[i] = 0;
    }
    return tab;
}

void libererTableauDynamique(int *tab) {
    free(tab);
}
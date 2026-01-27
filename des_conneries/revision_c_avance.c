/**
 * Révision C – Concepts avancés (~500 lignes)
 * Auteur : Révision C Avancée
 * Date : 20 janvier 2026
 * Compile avec : gcc -Wall -Wextra -std=c99 -DDEBUG -o revision_avance revision_c_avance.c
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <signal.h>
#include <setjmp.h>
#include <time.h>
#include <assert.h>

// === CONFIGURATION ===
#ifdef DEBUG
    #define DBG_PRINT(fmt, ...) fprintf(stderr, "[DEBUG] %s:%d: " fmt "\n", __FILE__, __LINE__, ##__VA_ARGS__)
#else
    #define DBG_PRINT(fmt, ...)
#endif

// === MACROS AVANCÉES ===
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))
#define STRINGIFY(x) #x
#define CONCAT(a, b) a##b

// Exemple de macro avec side effects contrôlés
#define SAFE_FREE(ptr) do { if (ptr) { free(ptr); (ptr) = NULL; } } while(0)

// === STRUCTURES AVANCÉES ===
typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct {
    char *name;
    int id;
    union {
        float salary;
        int hourly_rate;
    } pay;
    struct {
        unsigned int is_manager : 1;
        unsigned int active : 1;
        unsigned int reserved : 6;
    } flags;
} Employee;

// === PROTOTYPES ===
void fonctionRecursive(int n);
int factorielle(int n);
int fibonacci(int n);

// Pointeur de fonction
typedef int (*Operation)(int, int);
int add(int a, int b);
int mul(int a, int b);
int appliquer(Operation op, int x, int y);

// Liste chaînée
Node* creerNoeud(int val);
void insererDebut(Node **head, int val);
void afficherListe(Node *head);
void libererListe(Node **head);
int tailleListe(Node *head);

// Callback
void itererTableau(int *tab, size_t n, void (*callback)(int));

// Volatile
volatile sig_atomic_t signal_recu = 0;
void gestionnaireSignal(int sig);

// setjmp / longjmp
jmp_buf env;

// Bit-fields & union
void testerUnionEtBitfield(void);

// Sécurité mémoire
void copierNomSecurise(char *dest, const char *src, size_t taille_max);

// Statique interne
static int compteurAppel = 0;
void incrementerCompteur(void);

// Compilation conditionnelle
void fonctionConditionnelle(void);

// Gestion d'erreur avancée
void lireFichierSafely(const char *nom);

// === FONCTION PRINCIPALE ===
int main(void) {
    printf("=== RÉVISION C – CONCEPTS AVANCÉS ===\n\n");

    // 1. Récursivité
    printf("Factorielle de 5 : %d\n", factorielle(5));
    printf("Fibonacci(7) : %d\n", fibonacci(7));
    printf("Suite récursive descendante :\n");
    fonctionRecursive(3);

    // 2. Pointeurs de fonctions et callbacks
    Operation ops[2] = {add, mul};
    printf("\nAddition via pointeur : %d\n", appliquer(ops[0], 4, 5));
    printf("Multiplication via pointeur : %d\n", appliquer(ops[1], 4, 5));

    // 3. Liste chaînée
    Node *liste = NULL;
    insererDebut(&liste, 30);
    insererDebut(&liste, 20);
    insererDebut(&liste, 10);
    printf("\nListe chaînée : ");
    afficherListe(liste);
    printf("Taille : %d\n", tailleListe(liste));
    libererListe(&liste);

    // 4. Callback sur tableau
    int tab[] = {1, 2, 3, 4};
    printf("\nCallback (affichage x2) :\n");
    itererTableau(tab, ARRAY_SIZE(tab), [](int x) { printf("%d -> %d\n", x, x * 2); });

    // 5. Signal
    signal(SIGINT, gestionnaireSignal);
    printf("\nEn attente de SIGINT (Ctrl+C) pendant 3s... (simulation)\n");
    // On ne bloque pas vraiment, juste démo du mécanisme
    // Dans un vrai cas, on ferait pause() ou boucle

    // 6. setjmp / longjmp
    if (setjmp(env) == 0) {
        printf("\nPremier passage (normal)\n");
        longjmp(env, 1); // saut non local
    } else {
        printf("Retour via longjmp !\n");
    }

    // 7. Union + bit-field
    testerUnionEtBitfield();

    // 8. Sécurité chaîne
    char buffer[20];
    copierNomSecurise(buffer, "Jean Dupont", sizeof(buffer));
    printf("\nCopie sécurisée : '%s'\n", buffer);

    // 9. Variable statique
    for (int i = 0; i < 3; i++) {
        incrementerCompteur();
    }

    // 10. Compilation conditionnelle
    fonctionConditionnelle();

    // 11. Gestion d'erreur fichier
    lireFichierSafely("fichier_inexistant.txt");

    // 12. Macro avancée
    printf("\nMAX(10, 20) = %d\n", MAX(10, 20));
    printf("MIN(10, 20) = %d\n", MIN(10, 20));
    printf("Taille tableau local : %zu\n", ARRAY_SIZE(tab));
    printf("Stringify : %s\n", STRINGIFY(hello world));
    printf("Concat : %d\n", CONCAT(val, 1)); // val1 doit exister → on la crée :
    int val1 = 999;
    (void)val1; // éviter warning

    // 13. Assertion (désactivable avec -DNDEBUG)
    int x = 5;
    assert(x > 0);
    printf("\nAssertion réussie (x = %d > 0)\n", x);

    printf("\n=== FIN DES CONCEPTS AVANCÉS ===\n");
    return EXIT_SUCCESS;
}

// === DÉFINITIONS ===

// ---------- Récursivité ----------
void fonctionRecursive(int n) {
    if (n <= 0) {
        printf("Base case\n");
        return;
    }
    printf("Appel %d\n", n);
    fonctionRecursive(n - 1);
}

int factorielle(int n) {
    if (n < 0) return -1; // erreur
    if (n == 0 || n == 1) return 1;
    return n * factorielle(n - 1);
}

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// ---------- Pointeurs de fonctions ----------
int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

int appliquer(Operation op, int x, int y) {
    return op(x, y);
}

// ---------- Liste chaînée ----------
Node* creerNoeud(int val) {
    Node *n = malloc(sizeof(Node));
    if (!n) {
        perror("malloc noeud");
        exit(EXIT_FAILURE);
    }
    n->data = val;
    n->next = NULL;
    return n;
}

void insererDebut(Node **head, int val) {
    Node *nouveau = creerNoeud(val);
    nouveau->next = *head;
    *head = nouveau;
}

void afficherListe(Node *head) {
    while (head) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

void libererListe(Node **head) {
    while (*head) {
        Node *tmp = *head;
        *head = (*head)->next;
        free(tmp);
    }
}

int tailleListe(Node *head) {
    int c = 0;
    while (head) {
        c++;
        head = head->next;
    }
    return c;
}

// ---------- Callback ----------
void itererTableau(int *tab, size_t n, void (*callback)(int)) {
    for (size_t i = 0; i < n; i++) {
        callback(tab[i]);
    }
}

// ---------- Signal ----------
void gestionnaireSignal(int sig) {
    signal_recu = 1;
    DBG_PRINT("Signal %d reçu", sig);
    // Ne pas faire d'opérations non async-signal-safe ici !
}

// ---------- setjmp / longjmp ----------
// Déjà utilisé dans main

// ---------- Union + Bit-field ----------
void testerUnionEtBitfield(void) {
    Employee emp;
    emp.name = "Alice";
    emp.id = 101;
    emp.pay.salary = 4500.50f;
    emp.flags.is_manager = 1;
    emp.flags.active = 1;

    printf("\nEmployé : %s (ID=%d)\n", emp.name, emp.id);
    printf("Salaire : %.2f\n", emp.pay.salary);
    printf("Est manager : %s\n", emp.flags.is_manager ? "Oui" : "Non");
    printf("Actif : %s\n", emp.flags.active ? "Oui" : "Non");

    // Tester l'union : même mémoire
    emp.pay.hourly_rate = 30;
    printf("Taux horaire (même mémoire) : %d\n", emp.pay.hourly_rate);
}

// ---------- Sécurité mémoire ----------
void copierNomSecurise(char *dest, const char *src, size_t taille_max) {
    if (!dest || !src || taille_max == 0) return;
    strncpy(dest, src, taille_max - 1);
    dest[taille_max - 1] = '\0'; // toujours terminer
}

// ---------- Variable statique ----------
void incrementerCompteur(void) {
    compteurAppel++;
    printf("Nombre d'appels : %d\n", compteurAppel);
}

// ---------- Compilation conditionnelle ----------
void fonctionConditionnelle(void) {
#ifdef FEATURE_X
    printf("\nFeature X activée !\n");
#else
    printf("\nFeature X désactivée (définissez -DFEATURE_X pour activer)\n");
#endif

#ifdef DEBUG
    DBG_PRINT("Mode debug actif");
#endif
}

// ---------- Gestion d'erreur fichier ----------
void lireFichierSafely(const char *nom) {
    FILE *f = fopen(nom, "r");
    if (f == NULL) {
        fprintf(stderr, "Erreur d'ouverture de '%s': ", nom);
        perror(""); // affiche le message lié à errno
        // Alternative : fprintf(stderr, "%s\n", strerror(errno));
        return;
    }
    // ... lecture ...
    fclose(f);
}

// ---------- Fin du fichier ----------
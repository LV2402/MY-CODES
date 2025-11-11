#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 20

char production[MAX][MAX];
int n;

/* FIRST and FOLLOW result arrays */
char firstSet[26][MAX];
char followSet[26][MAX];

/* function declarations */
void findFirst(char, int);
void findFollow(char);
void addTo(char[], char);

int main() {
    int i;
    char ch;

    printf("Enter number of productions: ");
    scanf("%d", &n);

    printf("Enter productions in form A=BC or A=a or A=# (ε):\n");
    for (i = 0; i < n; i++) {
        scanf("%s", production[i]);
    }

    printf("\n--- FIRST sets ---\n");
    for (i = 0; i < n; i++) {
        ch = production[i][0];
        findFirst(ch, 0);
        printf("FIRST(%c) = { %s }\n", ch, firstSet[ch - 'A']);
    }

    printf("\n--- FOLLOW sets ---\n");
    for (i = 0; i < n; i++) {
        ch = production[i][0];
        findFollow(ch);
        printf("FOLLOW(%c) = { %s }\n", ch, followSet[ch - 'A']);
    }

    return 0;
}

/* Add symbol to a set without duplicates */
void addTo(char set[], char val) {
    int i;
    for (i = 0; set[i] != '\0'; i++) {
        if (set[i] == val)
            return;
    }
    set[i] = val;
    set[i + 1] = '\0';
}

/* FIRST calculation */
void findFirst(char c, int depth) {
    int i;

    /* If terminal */
    if (!isupper(c)) {
        addTo(firstSet[c - 'A'], c);
        return;
    }

    /* If non-terminal */
    for (i = 0; i < n; i++) {
        if (production[i][0] == c) {
            char next = production[i][2];

            /* epsilon production */
            if (next == '#') {
                addTo(firstSet[c - 'A'], '#');
            }
            /* terminal production */
            else if (!isupper(next)) {
                addTo(firstSet[c - 'A'], next);
            }
            /* non-terminal production */
            else {
                findFirst(next, depth + 1);
                strcat(firstSet[c - 'A'], firstSet[next - 'A']);
            }
        }
    }
}

/* FOLLOW calculation */
void findFollow(char c) {
    int i, j;

    /* Add $ for start symbol */
    if (production[0][0] == c)
        addTo(followSet[c - 'A'], '$');

    /* Scan all productions */
    for (i = 0; i < n; i++) {
        int len = strlen(production[i]);

        for (j = 2; j < len; j++) {

            if (production[i][j] == c) {

                if (production[i][j + 1] != '\0') {
                    char next = production[i][j + 1];

                    /* If next is terminal */
                    if (!isupper(next)) {
                        addTo(followSet[c - 'A'], next);
                    }
                    /* If next is non-terminal */
                    else {
                        strcat(followSet[c - 'A'], firstSet[next - 'A']);
                    }
                }
                /* If symbol is at end of production */
                else {
                    char lhs = production[i][0];
                    if (lhs != c)
                        strcat(followSet[c - 'A'], followSet[lhs - 'A']);
                }
            }
        }
    }
}

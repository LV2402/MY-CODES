#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 200  // bigger to print stack nicely

// Grammar (indices start at 1):
// 1. E -> E+T
// 2. E -> T
// 3. T -> T*F
// 4. T -> F
// 5. F -> (E)
// 6. F -> i
static const char *production[] = {
    " ",       // 0 (unused)
    "E->E+T",  // 1
    "E->T",    // 2
    "T->T*F",  // 3
    "T->F",    // 4
    "F->(E)",  // 5
    "F->i"     // 6
};

// ACTION/GOTO table for the above grammar (classic example)
// Rows = states 0..11; Cols = i  +  *  (  )  $  E  T  F
static const char *TABLE[12][9] = {
/*0*/ {"S5", "",   "",   "S4", "",   "",   "1", "2", "3"},
/*1*/ {"",   "S6", "",   "",   "",   "Acc","",  "",  ""},
/*2*/ {"",   "R2", "S7", "",   "R2", "R2", "",  "",  ""},
/*3*/ {"",   "R4", "R4", "",   "R4", "R4", "",  "",  ""},
/*4*/ {"S5", "",   "",   "S4", "",   "",   "8", "2", "3"},
/*5*/ {"",   "R6", "R6", "",   "R6", "R6", "",  "",  ""},
/*6*/ {"S5", "",   "",   "S4", "",   "",   "",  "9", "3"},
/*7*/ {"S5", "",   "",   "S4", "",   "",   "",  "",  "10"},
/*8*/ {"",   "S6", "",   "",   "S11","",   "",  "",  ""},
/*9*/ {"",   "R1", "S7", "",   "R1", "R1", "",  "",  ""},
/*10*/{"",   "R3", "R3", "",   "R3", "R3", "",  "",  ""},
/*11*/{"",   "R5", "R5", "",   "R5", "R5", "",  "",  ""}
};

// stack keeps: state, symbol, state, symbol, ... , state
// we will store as ints but print nicely.
int stackv[MAX];
int top = 0;  // index of top element

static int colIndex(char sym) {
    switch(sym){
        case 'i': return 0;
        case '+': return 1;
        case '*': return 2;
        case '(': return 3;
        case ')': return 4;
        case '$': return 5;
        case 'E': return 6;
        case 'T': return 7;
        case 'F': return 8;
        default: return -1;
    }
}

static void printStackNice(void){
    // print as [state symbol state symbol ... state]
    // we store: state(0), symbol('x'), state, ...
    // by convention we start with just state 0 on stack
    for (int i = 0; i <= top; i++){
        if (i % 2 == 0) printf("%d ", stackv[i]);            // state
        else            printf("%c ", (char)stackv[i]);      // symbol
    }
}

int main(){
    char input[256];
    printf("Grammar:\n");
    for (int k = 1; k <= 6; k++) printf("%d. %s\n", k, production[k]);

    printf("\nEnter input string (use i for id, end with $), e.g., i+i*i$ : ");
    scanf("%255s", input);

    // init stack with state 0
    top = 0;
    stackv[top] = 0;

    printf("\n%-26s %-20s %-20s\n", "Stack", "Input", "Action");
    while (1) {
        int state = stackv[top];    // top is always a state index
        char a = *input;            // current input symbol
        int c = colIndex(a);

        // print current stack and input:
        printStackNice();
        int pad = 26 - 2*(top+1); if (pad < 1) pad = 1;
        for (int i=0;i<pad;i++) putchar(' ');
        printf("%-20s ", input);

        if (c == -1) {
            printf("Error: invalid symbol '%c'\n", a);
            return 0;
        }

        const char *action = TABLE[state][c];
        if (!action || action[0] == '\0') {
            printf("Error: no action\n");
            return 0;
        }

        if (strcmp(action, "Acc") == 0) {
            printf("Accept\n\nInput string accepted successfully.\n");
            break;
        }

        if (action[0] == 'S') {
            // SHIFT: push symbol, push new state
            int nextState = atoi(action + 1); // <-- handles S10, S11 correctly
            printf("Shift '%c', goto %d\n", a, nextState);

            stackv[++top] = a;         // push terminal symbol
            stackv[++top] = nextState; // push state
            input++;                   // consume input symbol
        }
        else if (action[0] == 'R') {
            int prodNo = atoi(action + 1); // rule number
            const char *rhs = strchr(production[prodNo], '>') + 1;
            int rhsLen = (int)strlen(rhs);

            // Pop 2*rhsLen items (symbol+state per symbol)
            // For (E), rhsLen == 3; for E+T, rhsLen == 3; for i, rhsLen == 1
            for (int k = 0; k < rhsLen; k++) {
                // pop state
                if (top < 0) { printf("Error: stack underflow\n"); return 0; }
                top--;
                // pop symbol
                if (top < 0) { printf("Error: stack underflow\n"); return 0; }
                top--;
            }

            char A = production[prodNo][0];   // LHS
            int curState = stackv[top];       // now a state on top
            int gotoCol = colIndex(A);
            const char *go = TABLE[curState][gotoCol];

            if (!go || go[0] == '\0') {
                printf("Error: no GOTO for %c from state %d\n", A, curState);
                return 0;
            }
            int gotoState = atoi(go);
            printf("Reduce by %s, goto %d\n", production[prodNo], gotoState);

            stackv[++top] = A;         // push LHS symbol
            stackv[++top] = gotoState; // push new state
        }
        else {
            printf("Error: unknown action '%s'\n", action);
            return 0;
        }
    }
    return 0;
}

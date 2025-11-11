#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define STKSZ 100

char stackArr[STKSZ];
int top = -1;

void push(char c){ stackArr[++top] = c; }
char popc(){ return (top >= 0) ? stackArr[top--] : '\0'; }
char peek(){ return (top >= 0) ? stackArr[top] : '\0'; }

int isTerminal(char c){
    return (c=='i' || c=='+' || c=='*' || c=='(' || c==')' || c=='$');
}

void printStack(){
    for(int i=0;i<=top;i++) putchar(stackArr[i]);
}

int main(){
    char input[256];
    printf("Grammar used:\n");
    printf("E -> T Q\n");
    printf("Q -> + T Q | ε\n");
    printf("T -> F R\n");
    printf("R -> * F R | ε\n");
    printf("F -> ( E ) | i\n\n");

    printf("Enter input string using i for id and end with $ (e.g., i+i*i$): ");
    scanf("%255s", input);

    // initialize stack with $ and start symbol
    push('$');
    push('E');

    int ip = 0;
    printf("\n%-20s %-20s %-20s\n","Stack","Input","Action");
    while(1){
        char X = peek();
        char a = input[ip];

        // print current step
        char *inptr = input + ip;
        printStack(); printf("%*s", (int)(21 - (top+1)), "");
        printf("%-20s ", inptr);

        // acceptance
        if(X=='$' && a=='$'){
            printf("Accept\n");
            break;
        }

        // error
        if(X=='\0' || a=='\0'){
            printf("Error (empty)\n");
            return 0;
        }

        // if top is terminal
        if(isTerminal(X)){
            if(X==a){
                popc();
                ip++;
                printf("Match %c\n", a);
            }else{
                printf("Error: expected '%c'\n", X);
                return 0;
            }
            continue;
        }

        // top is nonterminal: choose production by LL(1) table
        if(X=='E'){
            // FIRST(E)=FIRST(T) -> { '(', 'i' }
            if(a=='(' || a=='i'){
                popc();
                // E -> T Q  (push in reverse order)
                push('Q'); push('T');
                printf("E -> TQ\n");
            }else{
                printf("Error: no rule for E with '%c'\n", a);
                return 0;
            }
        } else if(X=='Q'){
            // Q -> + T Q | ε ; FIRST(+TQ)={'+'}, FOLLOW(Q)={')','$'}
            if(a=='+'){
                popc();
                push('Q'); push('T'); push('+');
                printf("Q -> +TQ\n");
            } else if(a==')' || a=='$'){
                popc(); // Q -> ε
                printf("Q -> ε\n");
            } else {
                printf("Error: no rule for Q with '%c'\n", a);
                return 0;
            }
        } else if(X=='T'){
            // FIRST(T)=FIRST(F) -> { '(', 'i' }
            if(a=='(' || a=='i'){
                popc();
                push('R'); push('F');
                printf("T -> FR\n");
            } else {
                printf("Error: no rule for T with '%c'\n", a);
                return 0;
            }
        } else if(X=='R'){
            // R -> * F R | ε ; FIRST(*FR)={'*'}, FOLLOW(R)={')','+','$'}
            if(a=='*'){
                popc();
                push('R'); push('F'); push('*');
                printf("R -> *FR\n");
            } else if(a==')' || a=='+' || a=='$'){
                popc(); // R -> ε
                printf("R -> ε\n");
            } else {
                printf("Error: no rule for R with '%c'\n", a);
                return 0;
            }
        } else if(X=='F'){
            // F -> (E) | i
            if(a=='i'){
                popc();
                push('i');
                printf("F -> i\n");
            } else if(a=='('){
                popc();
                push(')'); push('E'); push('(');
                printf("F -> (E)\n");
            } else {
                printf("Error: no rule for F with '%c'\n", a);
                return 0;
            }
        } else {
            printf("Error: unknown stack symbol '%c'\n", X);
            return 0;
        }
    }

    printf("\nString accepted successfully!\n");
    return 0;
}

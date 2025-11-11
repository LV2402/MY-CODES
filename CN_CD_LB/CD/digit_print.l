/* 
-------------------- HOW TO RUN THIS LEX PROGRAM --------------------

1. Save the file as: digit_print.l

2. Run Lex:
       lex digit_print.l

3. Compile the generated C code:
       gcc lex.yy.c -o digit_print

4. Run the executable:
       ./digit_print

---------------------------------------------------------------------
*/

%{
    #include <stdio.h>
%}

/* ---------- LEX RULES ---------- */
%%
[0-9]      { printf("Digit "); }   // If the character is 0–9, print "Digit"
.|\n       { /* ignore all other characters */ }
%%

/* ---------- MAIN FUNCTION ---------- */
int main() {
    printf("Enter the string: ");
    yylex();                         // Start lexical analysis
    return 0;
}

int yywrap() {
    return 1;
}

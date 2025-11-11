/* 
-------------------- HOW TO RUN THIS LEX PROGRAM --------------------

1. Save this file as: star_token.l

2. Run Lex:
       lex star_token.l

3. Compile:
       gcc lex.yy.c -o star_token

4. Run:
       ./star_token

---------------------------------------------------------------------
*/

%{
    #include <stdio.h>
%}

/* ---------- LEX RULES ---------- */
%%
"3cse1"        { printf("*"); }        // When pattern "3cse1" is matched, print *
.|\n           { /* ignore other characters */ }
%%

/* ---------- MAIN FUNCTION ---------- */
int main() {
    printf("Enter the string: ");
    yylex();                           // Start lexical scanning
    return 0;
}

int yywrap() {
    return 1;
}

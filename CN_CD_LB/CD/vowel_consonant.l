/* 
-------------------- HOW TO RUN THIS LEX PROGRAM --------------------

1. Save this file as: vowel_consonant.l

2. Run lex:
       lex vowel_consonant.l

3. Compile the generated C file:
       gcc lex.yy.c -o vowel_consonant

4. Run the executable:
       ./vowel_consonant

---------------------------------------------------------------------
*/

%{
    // Global counters for vowels & consonants
    int vowels = 0, consonants = 0;
%}

/* ---------------- LEX RULES ---------------- */
%%
[aeiouAEIOU]      { vowels++; }              // Count vowels
[a-zA-Z]          { consonants++; }          // Count consonants
.|\n              { /* Ignore other chars */ }
%%

/* ---------------- MAIN FUNCTION ---------------- */
int main() {
    printf("Enter a string: ");
    yylex();                                // Start scanning

    printf("\nNumber of vowels: %d", vowels);
    printf("\nNumber of consonants: %d\n", consonants);
    return 0;
}

int yywrap() {
    return 1;
}

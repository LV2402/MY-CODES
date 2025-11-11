/* 
-------------------- HOW TO RUN THIS LEX PROGRAM --------------------

1. Save this file as: keyword_recognition.l

2. Run Lex:
       lex keyword_recognition.l

3. Compile:
       gcc lex.yy.c -o keyword_recognition

4. Run:
       ./keyword_recognition

5. Type/paste C code and press Ctrl+D to end input

---------------------------------------------------------------------
*/

%{
    #include <stdio.h>
    #include <string.h>

    int keyword_count = 0;

    // List of 32 C keywords
    char *keywords[] = {
        "auto", "break", "case", "char", "const", "continue", "default", "do",
        "double", "else", "enum", "extern", "float", "for", "goto", "if",
        "int", "long", "register", "return", "short", "signed", "sizeof",
        "static", "struct", "switch", "typedef", "union", "unsigned", "void",
        "volatile", "while"
    };

    // Function to check if a word is a keyword
    int isKeyword(char *word) {
        for (int i = 0; i < 32; i++) {
            if (strcmp(keywords[i], word) == 0)
                return 1;
        }
        return 0;
    }
%}

/* ---------------- LEX RULES ---------------- */
%%
[a-zA-Z_][a-zA-Z0-9_]* {
        // If identifier matches keyword, print and count
        if (isKeyword(yytext)) {
            printf("Keyword: %s\n", yytext);
            keyword_count++;
        }
}

.|\n   { /* ignore non-word characters */ }
%%

/* ---------------- MAIN FUNCTION ---------------- */
int main() {
    printf("Enter the C code (Ctrl+D to end input):\n\n");
    yylex();     // Start lexical analysis

    printf("\nTotal number of keywords: %d\n", keyword_count);
    return 0;
}

int yywrap() {
    return 1;
}

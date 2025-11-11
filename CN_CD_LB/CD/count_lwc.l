/* 
-------------------- HOW TO RUN THIS LEX PROGRAM --------------------

1. Save this file as: count_lwc.l

2. Run lex:
       lex count_lwc.l

3. Compile the generated C code:
       gcc lex.yy.c -o count_lwc

4. Run the program:
       ./count_lwc

---------------------------------------------------------------------
*/

%{
    int line_count = 0;
    int word_count = 0;
    int char_count = 0;
%}

/* Regular expressions */
%%
[^\t\n ]+       { word_count++; char_count += yyleng; }  // Any non-space sequence = word
\n              { line_count++; char_count++; }          // Count newline as 1 character
.               { char_count++; }                        // Count any other character
%%


int main() {
    printf("Enter text (press Ctrl+D to stop input):\n");
    yylex();       // start lex analysis

    printf("\nTotal Lines      : %d", line_count);
    printf("\nTotal Words      : %d", word_count);
    printf("\nTotal Characters : %d\n", char_count);

    return 0;
}

int yywrap() { return 1; }

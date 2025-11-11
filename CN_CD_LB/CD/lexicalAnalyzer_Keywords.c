#include <stdio.h>
#include <string.h>
#include <ctype.h>

// List of 32 C keywords
char keywords[32][10] = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "int", "long", "register", "return", "short", "signed", "sizeof",
    "static", "struct", "switch", "typedef", "union", "unsigned", "void",
    "volatile", "while"
};

// Check if a word is keyword
int isKeyword(char *word) {
    for (int i = 0; i < 32; i++) {
        if (strcmp(keywords[i], word) == 0)
            return 1;
    }
    return 0;
}

int main() {

    char input[1000], word[50];
    int i = 0, j = 0;

    printf("Enter the source code:\n");
    fgets(input, sizeof(input), stdin);

    printf("\nKeywords found:\n");

    while (input[i] != '\0') {

        // If the character is alphabetic → start reading a word
        if (isalpha(input[i])) {
            j = 0;

            // Read letters/digits to form a word
            while (isalnum(input[i])) {
                word[j++] = input[i++];
            }

            word[j] = '\0';

            // Check if keyword
            if (isKeyword(word))
                printf("%s\n", word);
        }
        else {
            // Move to next character if not a letter
            i++;
        }
    }

    return 0;
}

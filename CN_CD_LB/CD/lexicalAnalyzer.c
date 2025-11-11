#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>

// Check if ch is a delimiter
bool isDelimiter(char ch) {
    return (ch == ' ' || ch == '+' || ch == '-' || ch == '*' || ch == '/' ||
            ch == ',' || ch == ';' || ch == '>' || ch == '<' || ch == '=' ||
            ch == '(' || ch == ')' || ch == '{' || ch == '}' || ch == '[' ||
            ch == ']' || ch == '\n' || ch == '\t');
}

// Check if ch is an operator
bool isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/' ||
            ch == '>' || ch == '<' || ch == '=');
}

// Check if token is a keyword
bool isKeyword(char *str) {
    char keywords[32][10] = {
        "auto","break","case","char","const","continue","default","do",
        "double","else","enum","extern","float","for","goto","if","int",
        "long","register","return","short","signed","sizeof","static","struct",
        "switch","typedef","union","unsigned","void","volatile","while"
    };

    for (int i = 0; i < 32; i++) {
        if (strcmp(str, keywords[i]) == 0)
            return true;
    }
    return false;
}

// Check if valid identifier
bool isValidIdentifier(char *str) {
    if (!isalpha(str[0]))  // First character must be letter
        return false;
    for (int i = 1; i < strlen(str); i++) {
        if (!isalnum(str[i]))
            return false;
    }
    return true;
}

// Lexical analyzer function
void lexicalAnalyzer(char *str) {
    int left = 0, right = 0;
    int len = strlen(str);
    char subStr[100];

    while (right <= len) {
        if (!isDelimiter(str[right])) {
            right++;
        } else {
            if (left != right) { // Found a token
                strncpy(subStr, str + left, right - left);
                subStr[right - left] = '\0';

                if (isKeyword(subStr))
                    printf("Keyword: %s\n", subStr);
                else if (isValidIdentifier(subStr))
                    printf("Identifier: %s\n", subStr);
                else if (isdigit(subStr[0]))
                    printf("Numeric Literal: %s\n", subStr);
                else
                    printf("Invalid Token: %s\n", subStr);
            }

            if (isOperator(str[right])) {
                printf("Operator: %c\n", str[right]);
            } else if (str[right] != ' ' && str[right] != '\n' && str[right] != '\t') {
                printf("Delimiter: %c\n", str[right]);
            }

            right++;
            left = right;
        }
    }
}

// Main function
int main() {
    char input[1000];
    printf("Enter input code:\n");
    fgets(input, sizeof(input), stdin);

    printf("\nTokens Found:\n");
    lexicalAnalyzer(input);

    return 0;
}

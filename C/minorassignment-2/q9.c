#include <stdio.h>

int main() {
    char ch;
    printf("Enter the choice of the character: ");
    scanf("%c", &ch);
    
    int n = ch - 'A' + 1;

    for (int i = 1; i <= n; i++) {
        // Print ascending part
        for (int j = 1; j <= n - i + 1; j++) {
            printf("%c ", 'A' + j - 1);
        }
        // Print spaces in between
        for (int k = 1; k < 2 * (i - 1); k++) {
            printf("  ");
        }
        // Print descending part
        for (int j = n - i + 1; j >= 1; j--) {
            if (j == n) continue; 
            printf("%c ", 'A' + j - 1);
        }
        printf("\n");
    }

    return 0;
}

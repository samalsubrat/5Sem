#include <stdio.h>

int main() {
    int num;
    printf("Enter the number > ");
    scanf("%d", &num);
    printf("+-----------------------------------------+\n");

    // Print the multiples of the entered number
    printf("| ");
    for (int i = 1; i <= 10; i++) {
        printf("%3d ", num * i); 
    }
    printf("|\n");

    // Print the numbers 1 to 10
    printf("| ");
    for (int i = 1; i <= 10; i++) {
        printf("%3d ", i);
    }
    printf("|\n");

    // Print the number
    printf("| ");
    for (int i = 1; i <= 10; i++) {
        printf("%3d ", num);
    }
    printf("|\n");

    printf("+-----------------------------------------+\n");

    return 0;
}
   
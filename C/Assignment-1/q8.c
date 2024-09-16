//with math library
/*
#include <stdio.h>
#include <math.h>
int main() {
    int N, sum;
    printf("Enter a positive integer: ");
    scanf("%d", &N);
    sum = pow(N, 1) + pow(N, 2) + pow(N, 3);
    printf("Sum of N^1 + N^2 + N^3 = %d\n", sum);

    return 0;
}
*/

#include <stdio.h>

int main() {
    int N, sum;
    
    printf("Enter a positive integer: ");
    scanf("%d", &N);

    sum = N + (N * N) + (N * N * N);  // Manually calculating N^1, N^2, and N^3
    
    printf("Sum of N^1 + N^2 + N^3 = %d\n", sum);

    return 0;
}

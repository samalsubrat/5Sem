#include <stdio.h>

int main() {
    int Ia = 345;
    float Fb = 4.5;
    char Chvar = 'Z';

    printf("Ia: Value = %d, Address = %p\n", Ia, &Ia);
    printf("Fb: Value = %.1f, Address = %p\n", Fb, &Fb);
    printf("Chvar: Value = %c, Address = %p\n", Chvar, &Chvar);

    return 0;
}

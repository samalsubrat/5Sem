#include <stdio.h>

int main() {
    int a = 55, b = 105, c = 89, d = 68;
    int *pa = &a, *pb = &b, *pc = &c, *pd = &d;
    int *max = pa;

    if (*pb > *max) max = pb;
    if (*pc > *max) max = pc;
    if (*pd > *max) max = pd;

    printf("Maximum value: %d\n", *max);
    return 0;
}

#include <stdio.h>

int main() {
    int m = 10, n = 5;
    int *mp = &m, *np = &n;

    *mp = *mp + *np;  // m = 10 + 5 = 15
    *np = *mp - *np;  // n = 15 - 5 = 10

    printf("%d %d\n%d %d\n", m, *mp, n, *np);
    return 0;
}

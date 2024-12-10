#include <stdio.h>

int main() {
    int a[] = {0, 10, 20, 30, 40, 50, 60, 70, 80, 90};
    int n = sizeof(a) / sizeof(a[0]);

    for (int i = 0; i < n; i++) {
        printf("a[%d]: Value = %d, Address = %p\n", i, a[i], &a[i]);
    }

    return 0;
}

#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;
    printf("Before swap: x = %d, Address = %p, y = %d, Address = %p\n", x, &x, y, &y);
    swap(&x, &y);
    printf("After swap: x = %d, Address = %p, y = %d, Address = %p\n", x, &x, y, &y);

    return 0;
}

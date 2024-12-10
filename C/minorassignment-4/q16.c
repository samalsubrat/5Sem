#include <stdio.h>

int main() {
    int a[] = {1, 2, 3, 4};
    int b[] = {5, 6, 7, 8};
    int c[] = {9, 10, 11, 12};
    int d[] = {13, 14, 15, 16};
    int sum[4];
    int *p1 = a, *p2 = b, *p3 = c, *p4 = d, *ps = sum;

    for (int i = 0; i < 4; i++) {
        *(ps + i) = *(p1 + i) + *(p2 + i) + *(p3 + i) + *(p4 + i);
        printf("sum[%d] = %d\n", i, *(ps + i));
    }

    return 0;
}

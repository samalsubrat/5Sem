#include <stdio.h>

void arrayDifference(int p[], int sizeP, int q[], int sizeQ, int result[], int *resultSize) {
    *resultSize = 0;
    for (int i = 0; i < sizeP; i++) {
        int found = 0;
        for (int j = 0; j < sizeQ; j++) {
            if (p[i] == q[j]) {
                found = 1;
                break;
            }
        }
        if (!found) {
            result[*resultSize] = p[i];
            (*resultSize)++;
        }
    }
}

int main() {
    int p[] = {1, 2, 3, 4};
    int q[] = {2, 4, 5, 6};
    int result[10], resultSize;

    arrayDifference(p, 4, q, 4, result, &resultSize);

    printf("Difference: ");
    for (int i = 0; i < resultSize; i++) {
        printf("%d ", result[i]);
    }
    return 0;
}

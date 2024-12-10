#include <stdio.h>

void arrange(int *a, int *b) {
    if (*a > *b) {
        int temp = *a;
        *a = *b;
        *b = temp;
    }
}

int main() {
    int n1, n2, n3, n4, n5, n6;

    printf("Enter SIX numbers separated by blanks> ");
    scanf("%d %d %d %d %d %d", &n1, &n2, &n3, &n4, &n5, &n6);

    int *nums[] = {&n1, &n2, &n3, &n4, &n5, &n6};
    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 6; j++) {
            arrange(nums[i], nums[j]);
        }
    }

    printf("The numbers in ascending order are: %d %d %d %d %d %d\n", n1, n2, n3, n4, n5, n6);
    return 0;
}

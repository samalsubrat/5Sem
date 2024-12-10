#include <stdio.h>

int main() {
    int arr[] = {120, 502, 118, 188, 106, 447};
    int *ptr[] = {&arr[0], &arr[1], &arr[2], &arr[3], &arr[4], &arr[5]};
    int size = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < size; i++) {
        printf("arr[%d]: Value = %d, Address = %p\n", i, *ptr[i], ptr[i]);
    }

    return 0;
}

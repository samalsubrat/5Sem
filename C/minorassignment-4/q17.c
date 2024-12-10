#include <stdio.h>
#include <ctype.h>

int main() {
    char argv[][10] = {"mine", "cs", "oa"};  // Writable memory for strings
    int size = sizeof(argv) / sizeof(argv[0]);  // Number of strings

    for (int i = 0; i < size; i++) {
        for (char *p = argv[i]; *p != '\0'; p++) {
            *p = toupper(*p);  // Modify the string
        }
        printf("%s\n", argv[i]);  // Print the modified string
    }

    return 0;
}

#include <stdio.h>

struct Data {
    float x, y, z;
};

int main() {
    struct Data d = {6.7, 1.2, 2.3};
    struct Data *p = &d;

    printf("x = %.1f, y = %.1f, z = %.1f\n", p->x, p->y, p->z);

    return 0;
}

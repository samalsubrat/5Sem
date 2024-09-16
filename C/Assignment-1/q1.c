#include <stdio.h>

#define PI 3.141593

int main()
{
    int radius;
    float area, circumference;
    printf("Enter the value of the radius: ");
    scanf("%d", &radius);

    area = PI * radius * radius;
    circumference = 2 * PI * radius;
    printf("The area of the circle is: %.2f\n", area);
    printf("The circumference of the circle is: %.2f\n",circumference);
    return 0;
}


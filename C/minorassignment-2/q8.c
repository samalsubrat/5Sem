#include <stdio.h>
#include <math.h>

double naturalLog(double x) {
    double sum = 0;
    double term = (x - 1) / x;
    for (int i = 1; i <= 9; i++) {
        sum += pow(term, i) / i;
    }
    return sum;
}

int main() {
    double x;
    printf("Enter a value for x: ");
    scanf("%lf", &x);

    printf("Approximation of ln(x): %.2lf\n", naturalLog(x));
    return 0;
}

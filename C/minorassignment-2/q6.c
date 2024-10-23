#include <stdio.h>

int leap(int year){
    if (year%4==0 && (year % 100!=0 || year%400 == 0))
        return 1;
    return 0;
}

int dayNumber(int day, int month, int year){
    int daysMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if (leap(year)) {
        daysMonth[1] = 29; 
    }
    int dayNum = 0;
    for (int i = 0; i < month - 1; i++) {
        dayNum += daysMonth[i];
    }
    dayNum += day;
    return dayNum;
}

int main() {
    int day, month, year;
    printf("Enter day, month, and year: ");
    scanf("%d %d %d", &day, &month, &year);
    printf("Day number: %d\n", dayNumber(day, month, year));
    return 0;
}
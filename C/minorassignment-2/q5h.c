#include<stdio.h>
 int main(){
    int i=1;
    switch(i) {
        default: printf("Hello ");
        case 1: printf("Hello ");
        case 2:
        case 3: printf("Hello ");
    }
    return(0);
 }
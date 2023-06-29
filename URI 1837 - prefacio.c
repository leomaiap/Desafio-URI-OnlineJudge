#include <stdio.h>
#include <math.h>

int main(){
    int a, b, q, r;
    scanf("%d %d", &a, &b);
    r = a % b;
    q = a / b;
    printf("%d %d", q, r);
    
    return 0;
}
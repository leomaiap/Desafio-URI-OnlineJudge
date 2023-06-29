#include <stdio.h>
#include <math.h>

int main(){
    int  i;
    double x, n[100];
    scanf("%lf", &x);
    n[0] = x;
    for (i=1;i<=99;i++){
        n[i] = n[i-1]/2.0;
    }

    for (i=0;i<=99;i++){
        printf("N[%d] = %.4f\n", i, n[i]);
    }

    return 0;
}
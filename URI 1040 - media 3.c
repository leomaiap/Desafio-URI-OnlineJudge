#include <stdio.h>
#include <math.h>

int main(){
    double a, b, c, media;
    scanf("%lf", &a);
    scanf("%lf", &b);

    media = ((a*3.5)+(b*7.5))/11;

    printf("MEDIA = %.5f\n", media);

    return 0;
}
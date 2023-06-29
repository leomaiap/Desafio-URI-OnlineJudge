#include <stdio.h>
#include <math.h>

int main(){
    int d;
    float k, c;
    scanf("%d", &d);
    scanf("%f", &k);


    c = d/k;

    printf("%.3f km/l\n", c);
     
    return 0;
}
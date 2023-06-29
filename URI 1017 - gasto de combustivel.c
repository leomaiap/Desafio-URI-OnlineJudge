#include <stdio.h>


int main(){
    int tempo, velMed, dist;
    float gasto;
    scanf("%d", &tempo);
    scanf("%d", &velMed);

    dist = velMed * tempo;
    gasto = dist / 12.0;

    printf("%.3f", gasto);

    return 0;
}
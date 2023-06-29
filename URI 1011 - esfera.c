#include <stdio.h>
#include <math.h>
#define PI 3.14159

int main(){
    double raio, volume;
    scanf("%lf", &raio);

    volume = PI * (raio*raio*raio) * (4.0/3);

    printf("VOLUME = %.3f\n", volume);

    return 0;
}
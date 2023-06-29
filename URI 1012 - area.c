#include <stdio.h>
#include <math.h>
#define PI 3.14159

int main(){
    double a, b, c, reta, cir, tra, qua, ret, tri;
    scanf("%lf %lf %lf", &a, &b, &c);
    
    tri = (a*c)/2;
    cir = (c*c)*PI;
    tra = ((a+b)*c)/2;
    qua = b*b;
    reta = a*b;

    printf("TRIANGULO: %.3f\n", tri);
    printf("CIRCULO: %.3f\n", cir);
    printf("TRAPEZIO: %.3f\n", tra);
    printf("QUADRADO: %.3f\n", qua);
    printf("RETANGULO: %.3f\n", reta);

    return 0;
}
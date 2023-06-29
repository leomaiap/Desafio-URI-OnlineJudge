#include <stdio.h>
#include <math.h>

int main(){
    int id1, id2, quant1, quant2;
    double v1, v2, calc;
    scanf("%d %d %lf", &id1, &quant1, &v1);
    scanf("%d %d %lf", &id2, &quant2, &v2);

    calc = (quant1 * v1) + (quant2 * v2);

    printf("VALOR A PAGAR: R$ %.2f\n", calc);

    return 0;
}
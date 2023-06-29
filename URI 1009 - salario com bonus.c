#include <stdio.h>
#include <math.h>

int main(){
    double sal, vendas, bonus;
    char nome;
    scanf(" %s", &nome);
    scanf("%lf", &sal);
    scanf("%lf", &vendas);

    bonus = (vendas*0.15) + sal;

    printf("TOTAL = R$ %.2f\n", bonus);

    return 0;
}
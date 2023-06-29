#include <stdio.h>
#include <math.h>

int main(){
    int item, quant;
    float valor, tot;
    scanf("%d %d", &item, &quant);
    switch (item){
    case 1:
        valor = 4.0;
        break;
    case 2:
        valor = 4.5;
        break;
    case 3:
        valor = 5.0;
        break;
    case 4:
        valor = 2.0;
        break;
    case 5:
        valor = 1.5;
        break;
    default:
        break;
    }
    tot = valor*quant;
    printf("Total: R$ %.2f\n", tot);
    return 0;
}
#include <stdio.h>
#include <math.h>

int main(){
    int ini, fim, aux, soma = 0, i;
    scanf("%d", &ini);
    scanf("%d", &fim);
    if (ini > fim){
        aux = ini;
        ini = fim;
        fim = aux;
    }
    i = ini;
    while (i <= fim){
        if (i%13 != 0){
            soma += i;
        }
        i++;
    }
    printf("%d\n", soma);
    return 0;
}
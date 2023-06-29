#include <stdio.h>
#include <math.h>

int main(){
    int cont = 0, i = 0;
    float v, soma = 0, med;
    
    while (i != 6){
        scanf("%f", &v);
        if (v > 0){
            cont += 1;
            soma += v;
        }
        
        i++;
    }
    med = soma/cont;
    printf("%d valores positivos\n", cont);
    printf("%.1f\n", med);

    return 0;
}
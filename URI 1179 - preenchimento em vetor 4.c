#include <stdio.h>
//
// URI 1179 - Preenchimento em Vetor IV - Lista Exercicio - Vetores

int main(){
    int par[5], imp[5], Qpar = 0, Qimp = 0;
    int i, j, n;
    for (i=0;i<15;++i){
        scanf("%d", &n); //Ler 15 n int
        if (n % 2 == 0){ //n par faca
            par[Qpar] = n;
            Qpar++; // += 1
            if (Qpar == 5){ //Array de par chegou em 5, imprime, e zera par
                for (j = 0;j < 5;j++)
                   printf("par[%d] = %d\n", j, par[j]);
                Qpar = 0;
            }
        }else{
            imp[Qimp] = n;
            Qimp++;
            if (Qimp == 5){ //Array de impar chegou em 5, imprime, e zera impar
                for (j = 0;j < 5;j++)
                   printf("impar[%d] = %d\n", j, imp[j]);
                Qimp = 0;
            }
        }
    }
    for (j = 0;j < Qimp;j++) // Impares restantes
        printf("impar[%d] = %d\n", j, imp[j]);
    for (j = 0;j < Qpar;j++) // Pares restantes
        printf("par[%d] = %d\n", j, par[j]);
    
    return 0;
}

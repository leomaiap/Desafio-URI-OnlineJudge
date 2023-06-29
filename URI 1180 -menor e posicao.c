#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    int vet[n], i, menor, pos = 0;
    scanf("%d", &vet[0]);
    menor = vet[0];
    for (i=1;i<n;i++){
        scanf("%d", &vet[i]);
        if (vet[i]<menor){
            menor = vet[i];
            pos = i;
        }
    }
    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", pos);
    return 0;
}


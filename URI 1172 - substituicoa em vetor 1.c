#include <stdio.h>
#include <math.h>

int main(){
    int vetor[10];
    int i;
    for (i=0;i<=9;i++){
        scanf("%d", &vetor[i]);
        if (vetor[i]<=0){
            vetor[i] = 1;
        }
    }
    for (i=0;i<=9;i++){
        printf("X[%d] = %d\n", i, vetor[i]);
    }
    return 0;
}
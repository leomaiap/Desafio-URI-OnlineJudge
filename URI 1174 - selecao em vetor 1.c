#include <stdio.h>
#include <math.h>

int main(){
    float array[100], copy[100];
    int i, cont = 0, ind[100];
    for (i=0;i<=99;i++){
        scanf("%f", &array[i]);
        if (array[i] <= 10){
            cont += 1;
            copy[cont-1] = array[i];
            ind[cont-1] = i;
        }
    }
    for (i=0;i<=cont-1;i++){
        printf("A[%d] = %.2f\n", ind[i], copy[i]);
    }
    return 0;
}

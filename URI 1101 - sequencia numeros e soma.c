#include <stdio.h>
#include <math.h>

int main(){
    int m, n, soma, aux, i;
    scanf("%d %d", &m, &n);
    while (1){
        if (m <= 0 || n <= 0) break;
        if (m > n){
        aux = m;
        m = n;
        n = aux;
        }
        soma = 0;
        for (i=m; i <= n; i++){
            soma += i;
            printf("%d ", i);
        }

        printf("Sum=%d\n", soma);

        scanf("%d %d", &m, &n);

    }    
    return 0;
}
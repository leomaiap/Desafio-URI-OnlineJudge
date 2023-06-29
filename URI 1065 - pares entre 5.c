#include <stdio.h>
#include <math.h>

int main(){
    int n, i, cont = 0;
    for (i = 1; i <= 5; i++){
        scanf("%d", &n);
        if ((n%2) == 0)
            cont += 1;
    }
    printf("%d valores pares\n", cont);
    return 0;
}
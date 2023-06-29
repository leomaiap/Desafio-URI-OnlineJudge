#include <stdio.h>

int main(){
    int num, pos=0, neg=0, imp=0, par=0, i;
    for (i=1; i<=5; i++){
        scanf("%d", &num);
        if (num > 0)
            pos += 1;
        else if (num < 0 && num != 0)
            neg += 1;
        if (num%2 == 0)
            par += 1;
        else
            imp += 1;
    }
   
    printf("%d valor(es) par(es)\n", par);
    printf("%d valor(es) impar(es)\n", imp);
    printf("%d valor(es) positivo(s)\n", pos);
    printf("%d valor(es) negativo(s)\n", neg);
    
    return 0;
}
#include <stdio.h>
#include <math.h>

int main(){
    int testes;
    float div, x, y;
    scanf("%d", &testes);
    for (;testes > 0; testes--){
        scanf("%f %f", &x, &y);
        if (y == 0){
            printf("divisao impossivel\n");
        }else{
            div = x/y;
            printf("%.1f\n", div);
        }
    }
    return 0;
}
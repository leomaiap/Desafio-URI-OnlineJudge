#include <stdio.h>
#include <math.h>

int main(){
    int hi, hf, dif;
    scanf("%d %d", &hi, &hf);
    if (hi == hf){
        printf("O JOGO DUROU 24 HORA(S)\n");
    }else{
        dif = hf - hi;
        if (dif < 0){
        dif += 24;
    }
    printf("O JOGO DUROU %d HORA(S)\n", dif);
    }
    

    return 0;
}
#include <stdio.h>
#include <math.h>

int main(){
    int hi, hf, mi, mf, h ,m;
    scanf("%d %d %d %d", &hi, &mi, &hf, &mf);
    h = hf-hi;
    m = mf-mi;

    if (h < 0){
        h += 24;
    }
    if (m < 0){
        m += 60;
        h -= 1;
    }
    if (h < 0){
        h += 24;
    }

    if (m == 0 && h == 0){
        printf("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)");
    }else{
        printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)", h, m);
    }
    return 0;
}
#include <stdio.h>

int main(){
    int seg = 0, min = 0, hora = 0;
    scanf("%d", &seg);

    while(seg >= 60){
        min += 1;
        seg -= 60;
    }

    while (min >= 60){
        hora += 1;
        min -= 60;
    }
    printf("%d:%d:%d", hora, min, seg);
    return 0;
}
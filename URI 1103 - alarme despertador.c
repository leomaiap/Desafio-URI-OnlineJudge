#include <stdio.h>
#include <math.h>

int main(){
    int h1 = 1, m1, h2, m2, min;

    while (1){
        scanf("%d %d %d %d", &h1, &m1, &h2, &m2);
        if ((h1+h2+m1+m2) ==0)
            break;
        min = ((h2 - h1) * 60) - (m1 - m2);
        if (min < 0)
            min += 1440;
        printf("%d\n", min);

    }
    
     
    return 0;
}
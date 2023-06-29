#include <stdio.h>
#include <math.h>
/*
int main(){
    int t, i, x = 0;
    scanf("%d", &t);
    
    for (i=0;i<=999;i++){
        if (x == t){
            x = 0;
        }
        if (x == 0){
            printf("N[%d] = 0\n", i);
            x++;
        }else{
            printf("N[%d] = %d\n", i, x);
            x++;
        }
    }    

    return 0;
}*/

int main(){
    int t, i, x = 0, m[1000];
    scanf("%d", &t);
    
    for (i=0;i<=999;i++){
        if (x == t){
            x = 0;
        }
        if (x == 0){
            m[i] = x;
            x++;
        }else{
            m[i] = x;
            x++;
        }
    }    
    for (i=0;i<=999;i++){
        printf("N[%d] = %d\n", i, m[i]);
    }
    return 0;
}
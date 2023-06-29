#include <stdio.h>

int main(){
    int i, n, ip = 0;
    scanf("%d", &n);
    for (i = n; ip != 6; i++){
        if (i%2 ==1){
            printf("%d\n", i);
            ip++;
        }
    }
    return 0;
}
#include <stdio.h>
#include <math.h>

int main(){
    int i = 0, n, j;
    scanf("%d", &n);
    for (j=1; j <= n; j++){
        while (1){
            printf("%d %d %d PUM\n", i+1, i+2, i+3);
            i += 4;
            break;
        }
    }
        
    return 0;
}
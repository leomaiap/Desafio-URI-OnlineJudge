#include <stdio.h>
 
int main() {
    while (1){
        int n, i;
        scanf("%d", &n);
        if (n==0) break;
        for (i = 1; i <= n;i++){
            if (i == n)
                printf("%d\n", i);
            else
                printf("%d ", i);
        }
    }
    
    return 0;
}
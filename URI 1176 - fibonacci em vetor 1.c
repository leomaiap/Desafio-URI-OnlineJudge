#include <stdio.h>

int main(){
    int t, n, i;
    unsigned long long int fibo[61];
    
    fibo[0] = 0;
    fibo[1] = 1;

    for (i=1; i<=61;i++){
        fibo[i+1] = fibo[i] + fibo[i-1];
    }
    scanf("%d", &t);
    for (i=0; i<t;i++){
        scanf("%d", &n);
        printf("Fib(%d) = %llu\n", n, fibo[n]);
    }

    return 0;
}


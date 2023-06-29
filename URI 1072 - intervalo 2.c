#include <stdio.h>

int main(){
    int i, n, num, in=0, out=0;
    scanf("%d", &n);
    for (i=1; i <= n; i++){
        scanf("%d", &num);
        if (num >= 10 && num <= 20){
            in += 1;
        }else
            out += 1;
    }
    printf("%d in\n", in);
    printf("%d out\n", out);
    return 0;
}
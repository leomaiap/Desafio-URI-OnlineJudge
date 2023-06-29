#include <stdio.h>
#include <math.h>

int main(){
    int xi, yi, xf, yf, cross;
    scanf("%d %d %d %d", &xi, &yi, &xf, &yf);
    cross = abs(xf-xi) + abs(yf-yi);
    printf("%d\n", cross);
    return 0;
}
#include <stdio.h>
#include <math.h>

int main(){
    int l, c, i, j;
    int distancia, pokX, pokY, jogX, jogY;
    while(scanf("%d %d", &l, &c) != EOF){
        int grid[l][c];
        for (i=0;i<l;i++){
            for (j=0;j<c;j++){
                scanf("%d", &grid[i][j]);
                
            }
        }
        for (i=0;i<l;i++){
            for (j=0;j<c;j++){
                if (grid[i][j] == 1){
                    jogX = j;
                    jogY = i;
                }
                if (grid[i][j] == 2){
                    pokX = j;
                    pokY = i;
                }
            }
        }
        distancia = abs(jogX - pokX) + abs(jogY - pokY);
        printf("%d\n", distancia);
    }
    return 0;
}
#include <stdio.h>
#include <math.h>

int main(){
    int casos, j1, j2, i, mdc = 0;
    scanf("%d", &casos);
    for (i = 0; i < casos; i++){
        scanf("%d %d", &j1, &j2);

        while (j2 != 0){
            mdc = j1 % j2;
            j1 = j2;
            j2 = mdc;
        }
        printf("%d\n", j1);
    }
     
    return 0;
}
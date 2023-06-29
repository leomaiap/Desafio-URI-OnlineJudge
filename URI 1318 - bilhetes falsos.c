#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, m, i, j;
    while (n != 0 && m != 0){
        scanf("%d %d", &n, &m);
        int v[m];
        int rep = 0, igual = 0;
        for (i=0;i<m;i++){
            scanf("%d", &v[i]);
        }
        for (i=0;i<m;i++){
            igual = 0;
            for(j=i+1;j<m;j++){
                if (v[i] == v[j] && v[i] != 0 && v[j] != 0){
                    igual += 1;
                    v[j] = 0;
                }
            }
            if (igual > 0){
                rep += 1;
            }

        }    
    printf("%d\n", rep);
    }

    return 0;
}
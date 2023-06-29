#include <stdio.h>

int main(){
    int casos, n, i, j, aux;
    while(1){
        scanf("%d", &casos);
        if (casos == 0){
            break;
        }
        int suspeito[casos], pos[casos];
        for (i=0;i<casos;i++){
            scanf("%d", &suspeito[i]);
            pos[i] = i+1;
        }
        for (i=0;i<casos;i++){
            for (j=i+1;j<casos;j++){
                if (suspeito[i] > suspeito[j]){
                    aux = suspeito[i];
                    suspeito[i] = suspeito[j];
                    suspeito[j] = aux;
                    aux = pos[i];
                    pos[i] = pos[j];
                    pos[j] = aux;
                }
            }
        }
        printf("%d\n", pos[casos-2]);
       
    }
    return 0;
}
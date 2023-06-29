#include <stdio.h>
#include <math.h>

int main(){
    int s;
    while (1){
        scanf("%d", &s);
        if (s == 2002){
            printf("Acesso Permitido\n");
            break;
        }
        else{
            printf("Senha Invvalida\n");
        }
    }

    return 0;
}

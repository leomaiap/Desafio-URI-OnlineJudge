#include <stdio.h>


int main(){
    int n, i, caso;
    scanf("%d", &n);
    for (i = 1; i <= n; i++){
        scanf("%d", &caso);
        if (caso%2 == 0 && caso != 0){
            if (caso > 0) printf("EVEN POSITIVE\n");
            else printf("EVEN NEGATIVE\n");
        }else if(caso%2 !=0){
            if (caso > 0) printf("ODD POSITIVE\n");
            else printf("ODD NEGATIVE\n"); 
        }else if (caso == 0) printf("NULL\n");
    }

    return 0;
}
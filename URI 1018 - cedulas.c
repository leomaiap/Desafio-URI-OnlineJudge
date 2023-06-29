#include <stdio.h>
#include <math.h>

int main(){
    int n1, n2, n5, n10, n20, n50, n100, valor, valorIni;
    n1=n2=n5=n10=n20=n50=n100=0;
    
    scanf("%d", &valor);
    valorIni = valor;
    
    while (valor != 0){
        if (100 <= valor <= 10000000){
            n100 = valor/100;
            valor -= (n100*100);
        }
        if (50 <= valor <=99){
            n50 = valor/50;
            valor -= (n50*50);
        }
        if (20 <= valor <= 49){
            n20 = valor/20;
            valor -= (n20*20);
        }
        if (10 <= valor <= 19){
            n10 = valor/10;
            valor -= (n10*10);
        }
        if (5 <= valor <= 9){
            n5 = valor/5;
            valor -= (n5*5);
        }
        if (2 <= valor <= 4){
            n2 = valor/2;
            valor -= (n2*2);
        }
        if (valor == 1){
            n1 = valor/1;
            valor -= (n1*1);
        }
    }   
    //printf("%d nota(s) de R$ 100,00", n100);
    printf("%d\n", valorIni);
    printf("%d nota(s) de R$ 100,00\n", n100);
    printf("%d nota(s) de R$ 50,00\n", n50);
    printf("%d nota(s) de R$ 20,00\n", n20);
    printf("%d nota(s) de R$ 10,00\n", n10);
    printf("%d nota(s) de R$ 5,00\n", n5);
    printf("%d nota(s) de R$ 2,00\n", n2);
    printf("%d nota(s) de R$ 1,00\n", n1);
    
    return 0;
}
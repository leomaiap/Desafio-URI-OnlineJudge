#include <stdio.h>

int main(){
    float salario, novo, reaj;
    scanf("%f", &salario);
    if (salario <= 400){
        novo = salario + (salario*0.15);
        reaj = novo - salario;
        printf("Novo salario: %.2f\n", novo);
        printf("Reajuste ganho: %.2f\n", reaj);
        printf("Em percentual: 15 %%\n");
    }
    
    else if (salario > 400 && salario <= 800){
        novo = salario + (salario*0.12);
        reaj = novo - salario;
        printf("Novo salario: %.2f\n", novo);
        printf("Reajuste ganho: %.2f\n", reaj);
        printf("Em percentual: 12 %%\n");
    }
    
    else if (salario > 800 && salario <= 1200){
        novo = salario + (salario*0.1);
        reaj = novo - salario;
        printf("Novo salario: %.2f\n", novo);
        printf("Reajuste ganho: %.2f\n", reaj);
        printf("Em percentual: 10 %%\n");
    }
    
    else if (salario > 1200 && salario <= 2000){
        novo = salario + (salario*0.07);
        reaj = novo - salario;
        printf("Novo salario: %.2f\n", novo);
        printf("Reajuste ganho: %.2f\n", reaj);
        printf("Em percentual: 7 %%\n");
    }
    
    else if (salario > 2000){
        novo = salario + (salario*0.04);
        reaj = novo - salario;
        printf("Novo salario: %.2f\n", novo);
        printf("Reajuste ganho: %.2f\n", reaj);
        printf("Em percentual: 4 %%\n");
    }
    return 0;
}
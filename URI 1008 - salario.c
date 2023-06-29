#include <stdio.h>
#include <math.h>

int main(){
    int idFuncionario, horas;
    float salario, pag;
    scanf("%d", &idFuncionario);
    scanf("%d", &horas);
    scanf("%f", &salario);

    pag = salario * horas;

    printf("NUMBER = %d\n", idFuncionario);
    printf("SALARY = U$ %.2f\n", pag);


    return 0;
}
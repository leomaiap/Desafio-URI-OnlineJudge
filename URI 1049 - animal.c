#include <stdio.h>
#include <math.h>

int main(){
    char g, c, d;
    scanf(" %s", &g);
    scanf(" %s", &c);
    scanf(" %s", &d);

    if (g == "vertebrado"){
        if (c == "ave"){
            if (d == "carnivoro"){
                printf("aguia\n");
            }else{
                printf("pomba\n");
            }
        }else{
            if (d == "onivoro"){
                printf("homem\n");
            }else{
                printf("vaca\n");
            }
        }
    }

    if (g == "invertebrado"){
        if (c == "inseto"){
            if (d == "hematofago"){
                printf("pulga\n");
            }else{
                printf("lagarta\n");
            }
        }else{
            if (d == "hematofago"){
                printf("sanguessuga\n");
            }else{
                printf("minhoca\n");
            }
        }
    }

    return 0;
}
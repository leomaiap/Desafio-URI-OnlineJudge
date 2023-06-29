#include <stdio.h>
void bubbleSort(int *v, int n){
    int i, j;
    for (i=0;i<n;i++)
        for (j=i+1;j<n;j++){
            if(v[i]>v[j]){
                int temp = v[i];
                v[i] = v[j];
                v[j] = temp;
            }
        }
}
int main() {
    int n[3],nor[3],i;
    for(i = 0; i < 3; i++) scanf("%d", &n[i]);
    for(i = 0; i < 3; i++) nor[i] = n[i];
    bubbleSort(nor,3);
    for(i = 0; i < 3; i++) printf("%d\n", nor[i]);
    printf("\n");
    for(i = 0; i < 3; i++) printf("%d\n", n[i]);
    return 0;
}
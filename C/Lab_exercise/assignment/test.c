#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    int a;
    srand((unsigned)time(NULL));
    for(int i=0;i<5;i++){
        a=rand()%100;
        printf("%d\n",a);
    }
    return 0;
}

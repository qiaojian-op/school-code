#include <stdio.h>

int main()
{
    int a=1;
    int *p=&a;
    printf("%d\n",a);
    printf("%lu\n",p);
    return 0; 
}
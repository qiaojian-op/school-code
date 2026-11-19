#include <stdio.h>

int main()
{
    float number1,number2;
    number1=7.3;
    float *p1,*p2;
    p1=&number1;
    printf("number1=%.2f\n",*p1);
    p2=&number2;
    number2=*p1;
    printf("number2=%.2f\n",*p2);
    printf("The address of number1 is %p\n", (void*)p1);
    return 0;
}
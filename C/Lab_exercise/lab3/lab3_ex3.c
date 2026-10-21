#include <stdio.h>
float getInput(){
    float C;
    printf("Please enter the tempreture in degree Celcius: ");
    scanf("%f",&C);
    if (C<=0 || C>=100){
        printf("The value is illegle,please enter again!\n");
        return C=getInput();
    }
    else return C;
}
float C_to_F(float C){
    float F = 1.8 * C + 32;
    return F;
}
int main(){
    float c=getInput();
    float f=C_to_F(c);
    printf("The temperature from Celcius to Fahrenheit is: %.2f",f);
    return 0;
}
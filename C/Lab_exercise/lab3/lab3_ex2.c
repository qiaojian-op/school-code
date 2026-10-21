#include <stdio.h>
int height,length;
int area(int a,int b){
    return a*b;
}
int perimeter(int a,int b){{
    return 2*(a+b);
}}
int main(){
    printf("please enter the height: ");
    scanf("%d",&height);
    printf("please enter the length: ");
    scanf("%d",&length);
    int s=area(height,length);
    int c=perimeter(height,length);
    printf("Area: %d\n", s);
    printf("Perimeter: %d\n", c);
    return 0;
}
#include <stdio.h>
int main() {
    int a;
    printf("Please enter an integer: ");
    scanf("%d", &a);
    int ans;
    printf("The number of even numbers from 1 to %d is: ", a);
    if(a%2==0){
        ans=a/2;
    }
    else{
        ans=(a+1)/2;
    }
    printf("%d\n", ans);
    return 0;
}
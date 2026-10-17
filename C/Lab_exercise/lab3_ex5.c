#include <stdio.h>
         
void Calculate(int ans,int n){
    if(n==0){
        printf("%d",n);
    }
    else{
        return Calculate(ans+n,n-1);
    }
}

int main(){
    int n;
    scanf("%d",&n);
    Calculate(0,n);
    return 0;
}
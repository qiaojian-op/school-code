#include <stdio.h>

int nums[]={65,21,88,1,45,30,17,73,49,11};
int main(){
    int Max=nums[0];
    printf("The original array:\n");
    for(int i=0;i<10;i++){
        printf("%d ",nums[i]);
        if(Max<nums[i]){
            Max=nums[i];
        }
    }
    printf("\n");
    printf("The reversed array:\n");
    for(int i=9;i>=0;i--){
        printf("%d ",nums[i]);
        }
    printf("\nThe maximum number is %d\n",Max);
    return 0;
}
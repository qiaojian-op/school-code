#include <stdio.h>

int main()
{
    int nums[]={38,21,19,72,64,311,55,27,152,98};
    int size = sizeof(nums)/sizeof(nums[0]);
    int sum=0,sum_7=0;
    for(int i=0; i<size; i++){

        printf("%d ", nums[i]);
        sum += nums[i];
        if(nums[i] % 7 == 0){
            sum_7 += 1;
        }

    }
    printf("\nSum: %d", sum);
    printf("\nCount of multiples of 7: %d", sum_7);
    return 0;
}
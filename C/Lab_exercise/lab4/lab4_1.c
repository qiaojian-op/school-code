#include <stdio.h>

int main()
{
    int nums[10];
    nums[0]=1;
    for(int i=1;i < 10;i++ ){
        nums[i]=nums[i-1]+2;
    }
    for(int i=0;i < 10;i++ ){
        printf("%d %d\n",i,nums[i]);
    }
    return 0;
}
#include <stdio.h>

int main()
{
    char *pch,ch[100];

    printf("Enter a string: ");
    scanf("%s", ch);
    pch = ch;
    int size = strlen(ch);
    for(int i=size-1; i>=0; i--)
    {
        printf("%c", *(pch+i));
    }

    return 0;
}
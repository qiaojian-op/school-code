#include <stdio.h>

int main()
{
    int monthes[]={31,28,31,30,31,30,31,31,30,31,30,31};
    char *month_names[]={"January","February","March","April","May","June","July","August","September","October","November","December"};
    while(1){
        int month;
        printf("Enter month number (1-12): ");
        scanf("%d", &month);
        if(month < 1 || month > 12){
            printf("Invalid month number. Please try again.\n");
            continue;
        }
        printf("%s has %d days.\n", month_names[month-1], monthes[month-1]);
        break;
    }
    return 0;
}
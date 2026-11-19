#include <stdio.h>

char *name[]={"Ally","Bill","Carl","Dora"},*subject[]={"English","History","Physics"};
float score[4][3]={{68.5,85,71.3},{92.7,85.9,89.8},{88.2,77.5,75.9},{71,63.7,88.5}};

void Average_Marks_Students(){
    printf("Average marks of students:\n");
    for(int i=0;i<4;i++){
        float sum=0;
        for(int j=0;j<3;j++){
            sum+=score[i][j];
        }
        printf("%s %.1f\n",name[i],sum/3);
    }
}

void Average_Marks_Subjects(){
    printf("Average marks of subjects:\n");
    for(int j=0;j<3;j++){
        float sum=0;
        for(int i=0;i<4;i++){
            sum+=score[i][j];
        }
        printf("%s %.1f\n",subject[j],sum/4);
    }
}

int main()
{
    Average_Marks_Students();
    Average_Marks_Subjects();
    return 0;
}
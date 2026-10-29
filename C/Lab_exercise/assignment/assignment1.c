#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <math.h>

void menu(void);
void Practice(int level, int num);
void User_get(void);
bool check(int ans,int user_ans);
void Practice_creator(int level,int num);

void menu(void){
    printf("========Mayh Practice========\n");
    printf("Please choose a level\n");
    printf("LEVEL 1: 1\n");//'+':1 '-':2 0~10
    printf("LEVEL 2: 2\n");//'+':1 '-':2 0~100
    printf("LEVEL 3: 3\n");//'*':3 '/':4 0~100
    printf("==============================\n");
}

bool check(int ans,int user_ans){//判断答案
    return ans==user_ans;
}

void Practice_creator(int level,int num){
    int a,b,s1,s2,ans,user_ans,mark=0;
    srand((unsigned)time(NULL));//播种随机数
    if(level==1){//第一等级
        printf("Level 1 exercise: \n");
        for(int i=1;i<=num;i++){//生成题目
            a=rand()%10;
            b=rand()%10;
            s1=rand()%2;
            if (s1==1){//加法
                ans=a+b;
                printf("%d + %d = ?\nans: ",a,b);
                scanf("%d",&user_ans);
                if(check(ans,user_ans)==true){
                    mark++;
                    printf("Right!\n");
                }
                else{
                    printf("Wrong... the ans is %d\n",ans);
                }
            }
            if(s1==0){//减法
                if(a<b){//交换保证结果为正数
                    int x=b;
                    b=a;
                    a=x;
            }
                ans=a-b;
                printf("%d - %d = ?\nans:",a,b);
                scanf("%d",&user_ans);
                if(check(ans,user_ans)==true){
                    mark++;
                    printf("Right!\n");
                }
                else{
                    printf("Wrong... the ans is %d\n",ans);
                }
            }
//            printf("%d",s1);//debug
        }
        printf("Your mark is: %d of %d\n",mark,num);
        float m=(float)mark/num;
//        m/=num;
        printf("%f",m);//debug
        if(m-0.6>0){//pass
            printf("You pass this level.Let us challenge next level!\n");
            Practice_creator(level+1,num);
        }
        else {//fail
            printf("Don't worry!Let us practicre more!!!\n");
            Practice_creator(level,num);
        }
    }

    else if(level==2){
        printf("Level 2 exercise: \n");
        for(int i=1;i<=num;i++){//生成题目
            a=rand()%101;
            b=rand()%101;
            s1=rand()%2;
            if (s1==1){//加法
                ans=a+b;
                printf("%d + %d = ?\nans: ",a,b);
                scanf("%d",&user_ans);
                if(check(ans,user_ans)==true){
                    mark++;
                    printf("Right!\n");
                }
                else{
                    printf("Wrong... the ans is %d\n",ans);
                }
            }
            else{//减法
                if(a<b){//交换保证结果为正数
                    int x=b;
                    b=a;
                    a=x;
            }
                ans=a-b;
                printf("%d - %d = ?\nans: ",a,b);
                scanf("%d",&user_ans);
                if(check(ans,user_ans)==true){
                    mark++;
                    printf("Right!\n");
                }
                else{
                    printf("Wrong... the ans is %d\n",ans);
                }
            }
        }
        printf("Your mark is: %d / %d\n",mark,num); 
        float m;
        m=(float)mark/num;
        if(m-0.6>0){//pass
            printf("You pass this level.Let us challenge next level!\n");
            Practice_creator(level+1,num);
        }
        else{//fail
            printf("Don't worry!Let's practicre more!!!\n");
            Practice_creator(level,num);
        }
    }
    else if(level==3){
        printf("Level 3 exercise: \n");
        for(int i=1;i<=num;i++){//生成题目
            a=rand()%100;
            b=rand()%100;
            s1=rand()%2;
            s2=rand()%2;
            if (s1==1&&s2==1){//加法
                ans=a+b;
                printf("%d + %d = ?\nans: ",a,b);
                scanf("%d",&user_ans);
                if(check(ans,user_ans)==true){
                    mark++;
                    printf("Right!\n");
                }
                else{
                    printf("Wrong... the ans is %d\n",ans);
                }
            }
            else if(s1==1&&s2==0){//减法
                if(a<b){//交换保证结果为正数
                    int x=b;
                    b=a;
                    a=x;
            }
                ans=a-b;
                printf("%d - %d = ?\nans: ",a,b);
                scanf("%d",&user_ans);
                if(check(ans,user_ans)==true){
                    mark++;
                    printf("Right!\n");
                }
                else{
                    printf("Wrong... the ans is %d\n",ans);
                }
            }
            else if(s1==0&&s2==1){//乘法
                ans=a*b;
                printf("%d x %d = ?\n",a,b);
                printf("ans: ");
                scanf("%d",&user_ans);
                if(check(ans,user_ans)==true){
                    mark++;
                    printf("Right!\n");
                }
                else{
                    printf("Wrong... the ans is %d\n",ans);
                }
            }
            else if(s1==0&&s2==0){//除法
                double ansd,ansd_1,user_ansd;
                if(b==0) b+=10;
                ansd=(double) a/b;
                printf("%d / %d = ?\n",a,b);
                printf("ans: ");
                scanf("%lf",&user_ansd);
                if( fabs(user_ansd-ansd) <= 0.005 ){
                    mark++;
                    printf("You are right!\n");
                }
                else{
                    printf("Wrong... the ans is %.2f\n",ansd);
                }
            }
        }
        printf("Your mark is: %d / %d\n",mark,num); 
        float m;
        m=(float) mark/num;
        if(m-0.6>0){//pass
            printf("Amazing!!! You finish the final level!\n");
            Practice_creator(level+1,num);
        }
        else{//fail
            printf("Don't worry!Let's practicre more!!!\n");
            Practice_creator(level,num);
        }
    }
}

void Practice(int level,int num){
    if(level<1 || level >3 || num<25 || num>40){
        printf("Invalid Input!!");
        menu();
        User_get();
    }
    Practice_creator(level,num);
}

void User_get(){
    int level,num;
    printf("Please enter a number to chose level: ");
    scanf("%d",&level);
    printf("How many exercises do you want for each level?Please enter a number 25~40: ");
    scanf("%d",&num);
    Practice(level,num);
}

int main(){
    menu();
    User_get();
    return 0;
}

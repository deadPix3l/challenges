/* DalilyProgrammer - easy 267 - deadPix3l */
#include <stdio.h>
#define END 100

int main(int argc, char** argv)
{
    int x = 1; /* default value */
    printf("please enter 1-100: ");
    scanf("%d",&x);
    
    for(int i=1;i<=END;i++)
    {
        if(i==x) continue;
        switch(i%10) 
        {
            case 1: printf("%dst ",i); break;
            case 2: printf("%dnd ",i); break;
            case 3: printf("%drd ",i); break;
            default: printf("%dth ",i); break;
        }
    }
    return 0;
}
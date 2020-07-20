#include<stdio.h>
int main(){
    short i = 999;
    for(;i>=0;--i)
   {
       printf("%hi\t", i+1);
       if(i%5==0 )
       {
           printf("\n");
       }
   }
    return 0;
}

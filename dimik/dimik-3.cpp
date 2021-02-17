#include<iostream>
using namespace std;
int main()
{
    short i = 999;
    for(;i>=0;--i)
   {
       cout <<  i+1 << "\t";
       if(i%5==0 )
       {
           cout <<  '\n';
       }
   }
    return 0;
}

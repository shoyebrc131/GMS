#include <iostream>
using namespace std;
int main ()
{
    int repeat, innum, control, div = 1;
    cin >> repeat;
    for (control =1; control <= repeat; control++)
    {
       cin >> innum;
       cout << "Case " << control << ':';
       if (innum == 1)
       {
       cout << " 1" << endl;
       }
       else
       {
           div =1;
           while (div <= innum)
       {
           if (innum % div == 0)
           {
               cout << ' ' << div ;

           }
           div ++;
       }
       cout << endl;
       }
   }

}

#include <iostream>
using namespace std;
int main()
{
    int repeat, i, input,j;
    cin >> repeat;
    for ( i = 0; i < repeat; i++)
    {
        cin >> input;
        for (j = input; j >=0 ; j--)
         {
             if (j>1)
            {
                cout << 2 << "^" << j << " + ";
        }
            else if (j ==1)
            {
                cout << 2 << " + ";
            }
            else if (j == 0)
            {
                cout << 1 << endl;
            }
        }

    }
}

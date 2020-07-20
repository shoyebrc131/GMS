#include <iostream>
using namespace std;
int main()
{
    short repeat, i ;
    long x;
    cin >>repeat;
    for(i =0; i<repeat ; i++)
    {
        cin >> x;
        if (x%2 == 0)
        {
            cout << "even\n";
        }
        else
        {
            cout << "odd\n";
        }
    }
    return 0;
}

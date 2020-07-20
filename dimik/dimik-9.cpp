#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    unsigned short a, repeat, i;
    long input;

    cin >> repeat;
    for(i= 0; i < repeat; i++)
    {
        cin >> input;
        a = sqrt(input);
        if (a*a == input)
        {
            cout << "YES\n";
        }
        else
        {
            cout << "NO\n";
        }
    }
    return 0;
}

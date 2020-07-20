#include <iostream>
#include<cmath>
using namespace std;
int main()
{
    int repeat, i;
    float input;
    cin >> repeat;
    for ( i = 0; i < repeat; i++)
    {
        cin >> input;
        cout << ceil(log2(input)) << " days" << '\n';
    }
    return 0;
}

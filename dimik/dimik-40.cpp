#include <iostream>
#include<cmath>
using namespace std;
int main()
{
    int repeat, i, x, k ,sum;
    cin >> repeat;
    for ( i = 0; i < repeat; i++)
    {
        cin >> x >> k;
        k = k +1;
        sum = 1;
        while (--k)
        {
            sum = sum +  pow(x,k);
        }
        cout << "Result = " << sum << '\n';
    }
}

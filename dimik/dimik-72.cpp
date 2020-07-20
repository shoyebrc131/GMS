#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int repeat, i, a,b,c;
    float s, area;
    cout << fixed;
    cout.precision(2);
    cin >> repeat;
    for(i=0; i<repeat;i++)
        {
            cin >> a >> b >> c;
            s = (a + b + c)/2.0;
            area = sqrt(s*(s-a)*(s-b)*(s-c));
            if(area >= 0.0)
            {

                cout << area << endl;
            }
            else
            {
                 cout << "Oh, No!" << endl;
            }
        }
    return 0;
}


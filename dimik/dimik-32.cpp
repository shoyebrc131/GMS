#include <iostream>
using namespace std;
int main()
{
    int repeat, i, j, x, y;
    cin >> repeat;
    for(i=1;i<=repeat;i++)
    {
        cin >> x >> y;
        if (x>y)
        {
            cout << "Invalid!" <<endl;
        }
        else
        {
            for(j=0; j+x <= y; j = j+x)
        {
            cout << j+x <<endl;
        }
        }
     cout<<endl;
    }
    return 0;
}

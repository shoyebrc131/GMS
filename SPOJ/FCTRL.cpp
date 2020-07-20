#include <iostream>
#include <cmath>
using namespace std;
int main() {

    int repeat, innum, out, power, tmp;
    cin >> repeat;
    while(repeat--)
    {
        power = 1;
        out = 0;
        cin >> innum;
        tmp =innum/pow(5,power);
        while(tmp > 0)
        {
            out = out + tmp;
            power ++;
            tmp =innum/pow(5,power) ;
        }
        cout << out << endl;
    }
    return 0;
}

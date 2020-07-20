#include <iostream>
using namespace std;
int main()
{
    char input[200];
    short i =0 ;
	cin.getline( input,200);
	while (input[i] != '\0')
      i++;
    for(i = i -1; i>= 0;i-- )
        cout <<  input[i];
    cout << "\n";
    return 0;
}

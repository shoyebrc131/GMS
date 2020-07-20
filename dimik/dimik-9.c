#include <stdio.h>
#include <math.h>
int main()
{
    unsigned short a;
    char repeat, i;
    long input;

    scanf("%hhi", &repeat);
    for(i= 0; i < repeat; i++)
    {
        scanf("%li", &input);
        a = sqrt(input);
        if (a*a == input )
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}

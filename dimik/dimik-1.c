#include <stdio.h>
int main()
{
    short repeat, i ;
    long x;
    scanf("%hi", &repeat);
    for(i =0; i<repeat ; i++)
    {
        scanf("%li", &x);
        if (x%2 == 0)
        {
            printf("even\n");
        }
        else
        {
            printf("odd\n");
        }
    }
    return 0;
}

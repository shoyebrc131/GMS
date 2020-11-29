#include <stdio.h>
int main()
{
    char repeat,in;
    scanf("%hhi", &repeat);
    getchar();
    while(repeat--)
    {
        scanf("%c", &in);
        getchar();
        if (64 <in && in <91)
        {
            printf("Uppercase Character\n");
        }
        else if (96 <in && in <123)
        {
            printf("Lowercase Character\n");
        }
        else if (47 <in && in <58)
        {
            printf("Numerical Digit\n");
        }
        else
        {
            printf("Special Character\n");
        }
    }
    return 0;
}

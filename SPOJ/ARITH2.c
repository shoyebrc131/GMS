#include <stdio.h>
int main()
{
    int repeat, out, in;
    char car;
    scanf("%i\n",&repeat );
    while(repeat--)
    {
        scanf("%i\n",&out);
        car = 1;
        while(1)
        {
            scanf("%c",&car );
            if (car == '=')
            {
                break;
            }
            switch (car)
            {
                case '+': scanf("%i", &in);
                            out = out + in;
                            break;
                case '-': scanf("%i", &in);
                            out = out - in;
                            break;
                case '*': scanf("%i", &in);
                            out = out * in;
                            break;
                case '/' :scanf("%i", &in);
                            out = out / in;
                            break;
                default : break;
            }
        }
    printf("%i\n", out);
    }
}

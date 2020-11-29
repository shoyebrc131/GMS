#include <stdio.h>
int main() {

    int repeat, innum, out, tmp;
    scanf("%i", &repeat);
    while(repeat--)
    {
        out = 0;
        scanf("%i", &innum);
        while(innum)
        {
            innum = innum/5;
            out = out + innum;
        }
        printf("%i\n", out);
    }
    return 0;
}

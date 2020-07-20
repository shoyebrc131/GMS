#include <stdio.h>
int main()
{
    char input[1000];
    int repeat , j=0;
    unsigned short i =0 ;
    scanf("%d", &repeat);
    for (j =0 ; j < repeat; j++)
    {
        scanf("%s", input);
        i =0;
        while (input[i] != '\0')
            i++;
        while(i != 0)
        {   printf("%c", input[i]);
            i = i -1;
        }
        printf("%c\n",input[0]);
    }
    return 0;
}

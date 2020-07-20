#include <stdio.h>
int main()
{
    char input[200];
    short i =0;
	scanf("%[^\n]",&input);
    while (input[i] != '\0')
      i++;
    for(i = i -1; i>= 0;i-- )
        printf("%c", input[i]);
    printf("\n");
    return 0;
}

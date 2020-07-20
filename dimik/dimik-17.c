#include <stdio.h>
#include <string.h>
int main()
{
    unsigned char repeat, i;
    char instr[1000];
    unsigned short out =0, j;
    scanf("%hhu \n", &repeat);
    for(i =0; i < repeat; i++)
    {
        scanf("%[^\n] \n", &instr);
        for(j = 0; j < strlen(instr); j++)
        {
            if (instr[j] == 'a' || instr[j] == 'e' || instr[j] == 'i' || instr[j] == 'o' || instr[j] == 'u' || instr[j] == 'A' || instr[j] == 'E' || instr[j] == 'I' || instr[j] == 'O' || instr[j] == 'U')
            {
                out = out + 1;
            }
        }
    printf("Number of vowels = %hu \n", out);
    out = 0;
    }
    return 0;
}

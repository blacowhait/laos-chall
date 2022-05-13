#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char s[40];
    printf("input: ");
    scanf("%32s", s);
    if(!strcmp(s, "31337")){
        printf("Congratz!\nHere is your flag: LA2022{yeah_this_is_easier_than_C_0x??_series_LINZ_IS_HERE}\n");
    }
    return 0;
}

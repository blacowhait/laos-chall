#include <stdio.h>
#include <string.h>
#include <stdlib.h>

unsigned int arr[33] = {238, 202, 216, 198, 222, 218, 202, 190, 232, 222, 190, 228, 202, 236, 202, 228, 230, 210, 220, 206, 190, 152, 146, 156, 180, 190, 146, 166, 190, 144, 138, 164, 138};

int main(int argc, char const *argv[])
{
	unsigned int i = 0;
	char buf[36];

	printf("input: ");

	scanf("%36s", buf);

	if(strlen(buf)!=33){
		puts("invalid length.");
		exit(0);
	}

	while(i < 33){
		if(((int)buf[i]*2) != arr[i]){
			puts("nope.");
			exit(0);
		}
		i++;
	}
	printf("Congratz!\nHere is your flag: LA2022{%s}\n", buf);
	
	return 0;
}

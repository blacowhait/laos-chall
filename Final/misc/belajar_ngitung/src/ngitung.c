#include <stdio.h>
#include <stdlib.h>

void logo(){
  puts("██╗     ██╗███╗   ██╗███████╗");
  puts("██║     ██║████╗  ██║╚══███╔╝");
  puts("██║     ██║██╔██╗ ██║  ███╔╝ ");
  puts("██║     ██║██║╚██╗██║ ███╔╝  ");
  puts("███████╗██║██║ ╚████║███████╗");
  puts("╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝");
}

void alert(){
	puts("------------------------------ INFO ------------------------------");
	puts("Ayo kita bermain sebuah game menghitung");
	puts("Anak SD Bisa ini mah");
	puts("------------------------------ SEMANGAT ------------------------------");
}

void setup(){
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
}


int main(int argc, char const *argv[])
{
	setup();
	logo();
	alert();
	for (int i = 1; i < 5000; ++i)
	{
		int input;
		printf("Abis angka: %d Angka berapa? ", i);
		scanf("%d", &input);
		if(input != (i+1)){
			printf("Salah! Ayo coba belajar itung\n");
			exit(-1);
		}
	}
	printf("Congratulations ini flagnya LA2022{pwntools_master_jago_ngitungnya_LINZ_IS_HERE}");
	return 0;
}
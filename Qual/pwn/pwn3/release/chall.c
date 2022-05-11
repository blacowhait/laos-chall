#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

//gcc chall.c -fno-stack-protector -no-pie -z execstack -o hub_gua

void logo(){
  puts("██╗     ██╗███╗   ██╗███████╗");
  puts("██║     ██║████╗  ██║╚══███╔╝");
  puts("██║     ██║██╔██╗ ██║  ███╔╝ ");
  puts("██║     ██║██║╚██╗██║ ███╔╝  ");
  puts("███████╗██║██║ ╚████║███████╗");
  puts("╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝");
}

void alert(){
  puts("------------------- ALERT -------------------");
  puts("Yang mau serius di CSI tim gua kurang 1");
  puts("Tolong hub saya di discord Linz#7046");
  puts("Semangat BELAJARNYA");
  puts("------------------- THANKS -------------------");
  printf("\n");
}



void setup(){
  setvbuf(stdin,0,2,0);
  setvbuf(stdout,0,2,0);
}


int main(int argc, char **argv)
{
  setup();
  logo();
  char buffer[128];
  printf("Buffer: %p\n" , &buffer);
  puts("Can u get a full of control by hacking this program?");
  puts("No where to run");
  gets(buffer);
  return 0;
}
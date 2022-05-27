#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
//gcc fmt.c -no-pie -o string

void type(char str[]){
  int len = strlen(str);
  for(int i=0;i<len;i++) {
    putchar(str[i]);
    usleep(9000); //for Visual C
  }
}

void logo(){
  printf("\033[0;30m");
  type("██╗     ██╗███╗   ██╗███████╗\n");
  type("██║     ██║████╗  ██║╚══███╔╝\n");
  type("██║     ██║██╔██╗ ██║  ███╔╝ \n");
  type("██║     ██║██║╚██╗██║ ███╔╝  \n");
  type("███████╗██║██║ ╚████║███████╗\n");
  type("╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝\n");
}


void setup(){
  setvbuf(stdin,0,2,0);
  setvbuf(stdout,0,2,0);
}

int main(int argc, char **argv){

  setup();
  logo();

  char buf[128];
  char flag[128];
  char *flag_ptr = flag;

  memset(buf, 0, sizeof(flag));
  memset(buf, 0, sizeof(buf));

  puts("This time u can learn some string");
  
  FILE *file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("No file flag.txt \n");
    exit(0);
  }
  
  fgets(flag, sizeof(flag), file);
  
  while(1) {
    printf("> ");
    fgets(buf, sizeof(buf), stdin);
    printf(buf);
  }  
  return 0;
}
#include<stdio.h>

#define LINE "____________________________"
#define TITLE "C Programming in easy steps"

#ifdef _WIN32
#define SYSTEM "Windows"
#endif


int main()
{
    printf("\n \t %s \n \t %s \n", LINE, TITLE);
    printf("\t %s \n", LINE);
    printf("\n Operating System: %s \n", SYSTEM);

    return 0;
}
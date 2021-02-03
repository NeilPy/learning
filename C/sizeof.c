#include<stdio.h>
#include<limits.h>


int main() 
{
    printf("short int... \tsize: %d bytes %d байт \t", sizeof(short int));
    printf("от %d до %d", SHRT_MAX, SHRT_MIN);
}
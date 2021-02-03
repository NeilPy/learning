#include<stdio.h>
#include<limits.h>


int main() 
{
    printf("\nshort int... \tsize: %d bytes \t", sizeof(short int));
    printf("%d to %d", SHRT_MAX, SHRT_MIN);

    printf("\nlong int... \tsize: %d bytes \t", sizeof(char));
    printf("%d to %d", LONG_MAX, LONG_MIN);

    printf("\nchar... \tsize: %d bytes \n", sizeof(char));
    printf("float... \tsize: %d bytes \n", sizeof(float));
    printf("double... \tsize: %d bytes \n", sizeof(double));

    return 0;
}
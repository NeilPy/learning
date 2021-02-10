#include<stdio.h>


int main()
{
    int a = 4, b = 8, c = 2, d = 10;

    printf("Addition: %d \n", a + b);
    printf("Subtraction: %d \n", b - a);
    printf("Multiplication: %d \n", a * b);
    printf("Division: %d \n", b / a);
    printf("Modulus: %d \n", a % b);

    printf("Postfix increment: %d \n", c++);
    printf("Postfix now: %d \n", c);
    printf("Prefix increment: %d \n", ++d);
    printf("Prefix now: %d \n", d);

    return 0;
}
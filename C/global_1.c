#include<stdio.h>


static int sum = 100;


int main()
{
    // Выводит глобальную переменную sum
    extern int sum;
    printf("Sum is %d \n", sum);

    // Выводит глобальную переменную num которая находится в файле global_2
    extern int num;
    printf("Num in %d \n", num);

    return 0;
}
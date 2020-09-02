#include <stdio.h>
#include <math.h>

int is_in_range(float x){
    if(x>=0 || x<=1) return 1;
    return 0;
}

int main(void)
{
    float x;
    printf("Enter the value of x: ");
    scanf("%f", &x);

    switch (is_in_range(x))
    {
    case 1:
        printf("sin(%f)=%f\n", x, sin(x));
        break;
    
    default:
        printf("Wrong input\n");
        break;
    }

    return 0;
}

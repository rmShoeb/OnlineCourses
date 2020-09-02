#include <stdio.h>
#include <math.h>

int main(void){
    float x=0;

    printf("  x| sin(x)| cos(x)\n");
    while(x<=1){
        printf("%3.1f| %3.3f | %3.3f\n", x, sin(x), cos(x));
        x += 0.1;
    }
}
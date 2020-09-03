//preprocessors and macros
#include <stdio.h>
#include <stdlib.h>

int main(void){
    long long int total_weight = 0;     //variable to strore the total weight of the given seals
    int number_of_seal = 0;             //to store the number of seals
    int temp;                           //to read the data from file temporarily
    FILE *fp;                           //file pointer
    fp = fopen("seal.txt", "r");        //pointing to the file and configuring open mode

    while((fscanf(fp, "%d", &temp)!=EOF)){//read untill end of file
        total_weight += temp;
        number_of_seal++;
    }
    printf("Average weight of the seals: %0.2lf\n", (double)(total_weight/number_of_seal));//the average can be a floating point; using double for double precision

    fclose(fp);//closing the file
    return 0;
}
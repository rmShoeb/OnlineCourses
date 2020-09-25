#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double average(int input[], int input_size){
    int total=0;
    for(int i=0; i<input_size; i++){
        total += input[i];
    }
    return (double)total/(double)input_size;
}

int maximum(int input[], int input_size){
    int m = input[0];
    for(int i=1; i<input_size; i++){
        if(input[i]>m){
            m = input[i];
        }
    }
    return m;
}

int main(int argc, char const *argv[])
{
    int*    input;
    int     input_size;
    int     index=0;
    FILE*   file_pointer;

    file_pointer = fopen("input.txt", "r");
    if(file_pointer == NULL){
        printf("Failed to open file.\n");
        exit(1);
    }
    fscanf(file_pointer, "%d", &input_size);
    input   = (int*)malloc(sizeof(int)*4);
    while(fscanf(file_pointer, "%d", &input[index++]) != EOF);
    fclose(file_pointer);

    file_pointer = fopen("answer-hw3.txt", "a");
    printf("Average: %0.3lf\n", average(input, input_size));
    fprintf(file_pointer, "Average: %0.3lf\n", average(input, input_size));
    printf("Maximum: %d\n", maximum(input, input_size));
    fprintf(file_pointer, "Maximum: %d\n", maximum(input, input_size));
    fclose(file_pointer);

    return 0;
}

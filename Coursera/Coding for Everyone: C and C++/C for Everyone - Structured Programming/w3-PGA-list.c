#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char element_names[10][15] = {"Hydrogen", "Helium", "Lithium", "Berillium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Flourine", "Neon"};
char atomic_symbols[10][5] = {"H", "He", "Li", "Be", "B", "C", "N", "O", "Fl", "Ne"};
float weights[] = {1.008, 4.003, 6.941, 9.012, 10.811, 12.011, 14.007, 15.999, 18.998, 20.180};

typedef struct list{
    char    element_name[15];
    char    atomic_symbol[5];
    float   weight;
    struct list* next;
}list;

list* periodic_table_head = NULL;

void create_element_list(void){
    int i;
    list* pointer;

    periodic_table_head         = (list*)malloc(sizeof(list));
    strcpy(periodic_table_head->element_name, element_names[0]);
    strcpy(periodic_table_head->atomic_symbol, atomic_symbols[0]);
    periodic_table_head->weight = weights[0];
    pointer                     = periodic_table_head;

    for(i=1; i<10; i++){
        pointer->next           = (list*)malloc(sizeof(list));
        pointer                 = pointer->next;
        strcpy(pointer->element_name, element_names[i]);
        strcpy(pointer->atomic_symbol, atomic_symbols[i]);
        pointer->weight         = weights[i];
    }
}

void print_elements(void){
    list* pointer = periodic_table_head;
    int element_number = 1;
    printf("Atomic Number | Element Name | Atomic Symbol | Atomic Weight\n");
    printf("____________________________________________________________\n");
    while(pointer != NULL){
        printf("%13d |", element_number++);
        printf("%13s |", pointer->element_name);
        printf("%14s |", pointer->atomic_symbol);
        printf("%14.3f\n", pointer->weight);
        pointer = pointer->next;
    }
}


int main(void){    
    create_element_list();
    print_elements();

    return 0;
}

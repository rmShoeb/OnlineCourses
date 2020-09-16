#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define INSERT_N_ELEMENTS 200

typedef struct list{
    struct list* previous = NULL;
    int data;
    struct list* next = NULL;
}list;

list* head = NULL;

int random_data(void){return rand()%50;}

void create_list(void){
    int iter;
    list* pointer;
    list* temp;

    head            = (list*)malloc(sizeof(list));
    pointer         = head;
    pointer->data   = random_data();
    for(iter=1; iter<INSERT_N_ELEMENTS; iter++){
        pointer->next = (list*)malloc(sizeof(list));
        temp                = pointer;
        pointer             = pointer->next;
        pointer->data       = random_data();
        pointer->previous   = temp;
    }

    return;
}

void remove_duplicates(void){
    list* pointer = head;
    list* search_pointer;
    list* temp;
    int search_data;

    while(pointer != NULL){
        search_data     = pointer->data;
        search_pointer  = pointer->next;
        while(search_pointer != NULL){
            if(search_pointer->data == search_data){
                temp = search_pointer->previous;
                temp->next = search_pointer->next;
                search_pointer = search_pointer->next;
                search_pointer->previous = temp;
            }
            search_pointer = search_pointer->next;
        }
    }

    return;
}

void print_list(void){
    list* pointer   = head;
    int count       = 1;

    while(pointer != NULL){
        printf("%5d", pointer->data);
        pointer = pointer->next;
        if(count%10 == 0) printf("\n");
        count++;
    }
    printf("\n");
    return;
}

int main(void){
    srand(time(0));

    create_list();
    print_list();
    remove_duplicates();
    print_list();

    return 0;
}
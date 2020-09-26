#include <iostream>
#include <cstdlib>
#include <cstdbool>
#include <vector>
using namespace std;

void swap(int& a, int& b){
    int temp;
    temp = a;
    a = b;
    b = temp;
    return;
}

void min_heap(vector<int>& array, int new_element){
    /*
    Input:
    vector<int>& array  - array of integers containing the max-heap
    int new_element     - a new element that has to be inserted into the heap
    */
   bool heap_complete = false;
   int child_element_index;
   int parent_element_index;
   
   array.push_back(new_element);
   if(array.size() == 1) return;//if this is the only element, then what is the point to try to balance the heap?????

   child_element_index  = array.size()-1;
   while(!heap_complete){
       if(child_element_index%2 == 0) parent_element_index = (child_element_index/2)-1;
       else parent_element_index = (child_element_index-1)/2;
       
       if(array[parent_element_index] > array[child_element_index]) swap(array[parent_element_index], array[child_element_index]);
       else heap_complete = true;

       if(parent_element_index == 0) heap_complete = true;

       child_element_index = parent_element_index;
   }

    return;
}

void print_heap(vector<int>& heap){
    int iter;
    for(iter=0; iter<heap.size(); iter++)
        printf("%3d", heap[iter]);
    printf("\n");
    return;
}

int main(void){
    vector<int>heap;
    unsigned int new_element;

    while(true){
        cin >> new_element;
        if(new_element == -1) break;
        min_heap(heap,new_element);
    }
    print_heap(heap);

    return 0;
}

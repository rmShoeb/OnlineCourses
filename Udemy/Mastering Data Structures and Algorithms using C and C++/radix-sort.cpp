#include <iostream>
#include <cstdlib>
#include <cstdbool>
#include <vector>
#include <list>
#include <iterator>
#include <ctime>
using namespace std;



int maximum(vector<int>& data){
    int max = data[0];
    for(int iter=1; iter<data.size(); iter++){
        if(data[iter] > max) max = data[iter];
    }
    return max;
}

void swap(int &a, int &b){
    int temp;
    temp = a;
    a = b;
    b = temp;
    return;
}

void print(vector<int>& data){
    for(int iter=0; iter<data.size(); iter++)
        printf("%5d", data[iter]);
    printf("\n");
    return;
}

void radix_sort(vector<int>& data, bool reverse=false){
    int     iter;
    int     index;
    int     divident    = 1;
    bool    is_complete = false;
    int     max         = maximum(data);
    vector<list<int>> bins(10);

    while(!is_complete){
        for(iter=0; iter<data.size(); iter++){
            index = (data[iter]/divident)%10;
            bins[index].push_back(data[iter]);
        }
        index=0;
        for(iter=0; iter<10; iter++){
            while(!bins[iter].empty()){
                data[index] = bins[iter].front();
                bins[iter].pop_front();
            }
        }
        divident *= 10;
        if((max/divident)%10 == 0) is_complete = true;
    }

    if(reverse){
        for(iter=0; iter<data.size()/2; iter++)
            swap(data[iter], data[data.size()-1-iter]);
    }
    return;
}


int main(void){
    srand(1);

    vector<int> data;
    int iter;

    for(iter=0; iter<10; iter++)
        data.push_back(rand()%1000);
    print(data);
    radix_sort(data);
    print(data);
    return 0;
}
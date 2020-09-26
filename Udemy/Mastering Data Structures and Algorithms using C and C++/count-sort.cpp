#include <iostream>
#include <cstdbool>
#include <vector>
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

void count_sort(vector<int>& data, bool reverse=false){
    int iter, i;
    int maximum_value = maximum(data);
    int element_count[maximum_value+1] = {0};

    for(iter=0; iter<data.size(); iter++) element_count[data[iter]]++;
    i = 0;
    for(iter=0; iter<=maximum_value; iter++){
        while(element_count[iter] != 0){
            data[i] = iter;
            i++;
            element_count[iter]--;
        }
    }
    if(reverse){
        for(iter=0; iter<data.size()/2; iter++)
            swap(data[iter], data[data.size()-1-iter]);
    }
    return;
}

void print(vector<int>& data){
    for(int iter=0; iter<data.size(); iter++)
        printf("%3d", data[iter]);
    printf("\n");
    return;
}

int main(void){
    vector<int> data;
    int temp;
    int iter;

    for(iter=0; iter<10; iter++){
        cin >> temp;
        data.push_back(temp);
    }
    count_sort(data, true);
    print(data);
    return 0;
}
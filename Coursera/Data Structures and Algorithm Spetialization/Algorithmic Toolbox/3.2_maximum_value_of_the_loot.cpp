#include <iostream>
#include <vector>
#include<cstdio>
using std::vector;

int maxUnitValueIndex(double valuePerUnit[], int length){
  int max = 0;
  for(int i=1; i<length; i++){
    if(valuePerUnit[i] > valuePerUnit[max]) max = i;
  }
  return max;
}

bool allTaken(double valuePerUnit[], int length){
  for(int i=0; i<length; i++){
    if(valuePerUnit[i] != 0) return false;
  }
  return true;
}

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double value = 0.0;
  int length = weights.size();
  double valuePerUnit[length];
  int i;
  int indexMaxUnitValue;

  for(i=0; i<length; i++){
    valuePerUnit[i] = (double)values[i]/(double)weights[i];
  }

  while(capacity>0){
    indexMaxUnitValue = maxUnitValueIndex(valuePerUnit, length);
    if(weights[indexMaxUnitValue] <= capacity){
      value += (double)values[indexMaxUnitValue];
      capacity -= weights[indexMaxUnitValue];
    }
    else{
      value += (valuePerUnit[indexMaxUnitValue]*(double)capacity);
      capacity = 0;
    }
    valuePerUnit[indexMaxUnitValue] = 0;
    if(allTaken(valuePerUnit, length)) break;
  }

  return value;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  // std::cout.precision(10);
  // std::cout << optimal_value << std::endl;
  printf("%0.5f\n", optimal_value);
  return 0;
}

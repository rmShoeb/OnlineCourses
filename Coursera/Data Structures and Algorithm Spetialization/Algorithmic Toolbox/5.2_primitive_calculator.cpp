#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

int min(int a[], int size){
  int temp = a[0];
  for(int i=1; i<size; i++){
    if(temp>a[i] && a[i]!=0){
      temp = a[i];
    }
  }
  return temp;
}

vector<int> mySequence(int n){
  std::vector<int> dynamic;
  std::vector<int> sequence;
  int iter;
  int tempSize;

  dynamic.push_back(0);
  dynamic.push_back(0);

  for(iter=2; iter<=n; iter++){
    int temp[3] = {0};
    temp[0] = dynamic[iter-1]+1;
    if(iter%2 == 0){
      temp[1] = dynamic[iter/2]+1;
    }
    if(iter%3 == 0){
      temp[2] = dynamic[iter/3]+1;
    }
    dynamic.push_back(min(temp, 3));
  }

  // for(iter=0; iter<=n; iter++) std::cout << dynamic[iter] << " ";
  // std::cout << "\n";

  sequence.push_back(n);
  int count = dynamic[n]-1;
  for(iter=n; iter>0; iter--){
    if(dynamic[iter] == count){
      sequence.push_back(iter);
      count--;
    }
  }

  reverse(sequence.begin(), sequence.end());
  return sequence;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> sequence = mySequence(n);
  std::cout << sequence.size() - 1 << std::endl;
  for (size_t i = 0; i < sequence.size(); ++i) {
    std::cout << sequence[i] << " ";
  }
  std::cout << "\n";

  return 0;
}

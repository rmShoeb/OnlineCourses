#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;

int get_majority_element(vector<int> &a, int left, int right) {
  if (left == right) return -1;
  if (left + 1 == right) return a[left];
  //write your code here
  return -1;
}

bool isThereAnyMajority(vector<int> &a){
  sort(a.begin(), a.end());
  int iter;
  int count=1;

  for(iter=1; iter<a.size(); iter++){
    if(a[iter-1] != a[iter]) count = 1;
    else count++;
    if(count > (a.size()/2)) return true;
  }
  return false;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  // std::cout << (get_majority_element(a, 0, a.size()) != -1) << '\n';
  std::cout << isThereAnyMajority(a) << "\n";
}

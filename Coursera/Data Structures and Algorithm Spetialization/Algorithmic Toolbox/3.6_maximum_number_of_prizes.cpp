#include <iostream>
#include <vector>

using std::vector;

vector<int> optimal_summands(int n) {
  vector<int> summands;
  int iter;
  if(n<3) summands.push_back(n);
  else{
    iter = 1;
    while(n != 0){
      if(n<iter) break;
      summands.push_back(iter);
      n -= iter;
      iter++;
    }
    summands[summands.size()-1] += n;
  }
  return summands;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> summands = optimal_summands(n);
  std::cout << summands.size() << '\n';
  for (size_t i = 0; i < summands.size(); ++i) {
    std::cout << summands[i] << ' ';
  }
}

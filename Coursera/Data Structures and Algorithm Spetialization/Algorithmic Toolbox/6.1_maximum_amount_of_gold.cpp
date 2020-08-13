#include <iostream>
#include <vector>

using std::vector;

int max(int a, int b){
  if(a>b) return a;
  return b;
}

int optimal_weight(int W, const vector<int> &w){
  int numberOfItems = w.size();
  int i,j;
  vector<vector<int>> dynamic(numberOfItems+1, vector<int>(W + 1));

  for(i=0; i<=numberOfItems; i++){
    for(j=0; j<=W; j++){
      if(i==0 || j==0) dynamic[i][j] = 0;
      else if(w[i-1] <= j){
        dynamic[i][j] = max(dynamic[i-1][j], w[i-1]+dynamic[i-1][j-w[i-1]]);
      }
      else dynamic[i][j] = dynamic[i-1][j];
    }
  }

  return dynamic[numberOfItems][W];
}

int main() {
  int n, W;
  std::cin >> W >> n;
  vector<int> w(n);
  for (int i = 0; i < n; i++) {
    std::cin >> w[i];
  }
  std::cout << optimal_weight(W, w) << '\n';
}
//needed a little help from other participants

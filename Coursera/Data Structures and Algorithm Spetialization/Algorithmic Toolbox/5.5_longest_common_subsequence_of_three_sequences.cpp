#include <iostream>
#include <vector>

using std::vector;

int lcs3(vector<int> &a, vector<int> &b, vector<int> &c) {
  int dynamic[a.size()+1][b.size()+1][c.size()+1];
  int i, j, k;
  int max;

  for(i=0; i<=a.size(); i++){
    for(j=0; j<=b.size(); j++){
      for(k=0; k<=c.size(); k++){
        if(i==0 || j==0 || k==0) dynamic[i][j][k] = 0;
        else if((a[i-1] == b[j-1]) && (a[i-1] == c[k-1])){
          dynamic[i][j][k] = dynamic[i-1][j-1][k-1]+1;
        }
        else{
          max = dynamic[i-1][j][k];
          if(max < dynamic[i][j-1][k]) max = dynamic[i][j-1][k];
          if(max < dynamic[i][j][k-1]) max = dynamic[i][j][k-1];
          dynamic[i][j][k] = max;
        } 
      }
    }
  }
  return dynamic[a.size()][b.size()][c.size()];
}

int main() {
  size_t an;
  std::cin >> an;
  vector<int> a(an);
  for (size_t i = 0; i < an; i++) {
    std::cin >> a[i];
  }
  size_t bn;
  std::cin >> bn;
  vector<int> b(bn);
  for (size_t i = 0; i < bn; i++) {
    std::cin >> b[i];
  }
  size_t cn;
  std::cin >> cn;
  vector<int> c(cn);
  for (size_t i = 0; i < cn; i++) {
    std::cin >> c[i];
  }
  std::cout << lcs3(a, b, c) << std::endl;
}
//took a little help from geeksforgeeks

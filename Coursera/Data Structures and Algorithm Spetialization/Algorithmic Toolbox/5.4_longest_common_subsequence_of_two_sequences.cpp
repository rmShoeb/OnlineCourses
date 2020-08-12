#include <iostream>
#include <vector>

using std::vector;
int max(int a, int b, int c){
  if(a>b){
    if(a>c) return a;
    return c;
  }
  else{
    if(b>c) return b;
    return c;
  }
}

int lcs2(vector<int> &a, vector<int> &b) {
  int dynamic[a.size()+1][b.size()+1];
  int i, j;

  for(i=0; i<=a.size(); i++) dynamic[i][0] = 0;
  for(i=0; i<=b.size(); i++) dynamic[0][i] = 0;
  for(i=1; i<=a.size(); i++){
    for(j=1; j<=b.size(); j++){
      if(a[i-1] == b[j-1]){
        dynamic[i][j] = dynamic[i-1][j-1]+1;
      }
      else{
        dynamic[i][j] = max(dynamic[i-1][j], dynamic[i-1][j-1], dynamic[i][j-1]);
      }
    }
  }
  return dynamic[a.size()][b.size()];
}

int main() {
  size_t n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> a[i];
  }

  size_t m;
  std::cin >> m;
  vector<int> b(m);
  for (size_t i = 0; i < m; i++) {
    std::cin >> b[i];
  }

  std::cout << lcs2(a, b) << std::endl;
}

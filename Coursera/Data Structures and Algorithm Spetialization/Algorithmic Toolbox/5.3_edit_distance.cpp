#include <iostream>
#include <string>

using std::string;

int min(int a[]){
  int temp = a[0];
  for(int i=1; i<3; i++){
    if(temp>a[i]) temp = a[i];
  }
  return temp;
}

int edit_distance(const string &str1, const string &str2) {
  int dynamic[str1.length()+1][str2.length()+1];
  int i, j;
  int compute[3];

  for(i=0; i<=str1.length(); i++){
    dynamic[i][0] = i;
  }
  for(i=0; i<=str2.length(); i++){
    dynamic[0][i] = i;
  }
  for(i=1; i<=str1.length(); i++){
    for(j=1; j<=str2.length(); j++){
      compute[0] = dynamic[i-1][j]+1;
      compute[1] = dynamic[i][j-1]+1;
      if(str1[i-1] == str2[j-1]) compute[2] = dynamic[i-1][j-1];
      else compute[2] = dynamic[i-1][j-1]+1;
      dynamic[i][j] = min(compute);
    }
  }

  return dynamic[str1.length()][str2.length()];
}

int main() {
  string str1;
  string str2;
  std::cin >> str1 >> str2;
  std::cout << edit_distance(str1, str2) << std::endl;
  return 0;
}

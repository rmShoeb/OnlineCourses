#include <iostream>
using namespace std;

int min(int a[]){
  int temp = a[0];
  for(int i=1; i<3; i++){
    if(temp>a[i] && a[i]!=0){
      temp = a[i];
    }
  }
  return temp;
}

int get_change(int m) {
  int moneyArray[m+1] = {0};
  int temp[3] = {0};

  for(int i=1; i<=m; i++){
    temp[0] = moneyArray[i-1]+1;
    if(i>2){
      temp[1] = moneyArray[i-3]+1;
    }
    if(i>3){
      temp[2] = moneyArray[i-4]+1;
    }
    moneyArray[i] = min(temp);
  }

  return moneyArray[m];
}

int main() {
  int m;
  cin >> m;
  cout << get_change(m) << '\n';
}

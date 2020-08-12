#include <iostream>
using namespace std;


int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}

void swap(int &a, int &b){
  int temp = a;
  a = b;
  b = temp;
}

int gcdFast(int a, int b){
  if(a == 0) return b;
  else if(b == 0) return a;

  if(b > a) swap(a, b);
  int temp;
  while(b!=0){
    temp = b;
    b = a%b;
    a = temp;
  }
  return a;
}

int main() {
  int a, b;
  cin >> a >> b;
  // cout << gcd_naive(a, b) << endl;
  // swap(a, b);
  cout << gcdFast(a, b) << endl;
  return 0;
}

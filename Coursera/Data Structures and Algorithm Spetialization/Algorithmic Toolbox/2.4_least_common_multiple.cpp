#include <iostream>
using namespace std;

void swap(int &a, int &b){
  int temp = a;
  a = b;
  b = temp;
}

int gcd(int a, int b){
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

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

long long int lcmFast(int a, int b){
  if(a==0) return 0;
  else if(b==0) return 0;
  else return ((long long int)a/(long long int)gcd(a, b))*(long long int)b;
}
int main() {
  int a, b;
  cin >> a >> b;
  // cout << lcm_naive(a, b) << endl;
  cout << lcmFast(a, b) << endl;
  return 0;
}

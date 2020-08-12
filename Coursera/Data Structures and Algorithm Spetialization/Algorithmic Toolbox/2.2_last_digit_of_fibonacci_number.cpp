#include <iostream>
using namespace std;

int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;
}

int fibonacciLastDigitFast(int n){
    if(n>1){
        int previous = 0;
        int current = 1;
        int iter;
        int temp;

        for(iter=2; iter<=n; iter++){
            temp = previous;
            previous = current;
            current = (temp+previous)%10;
        }
        return current;
    }
    else{
        return n;
    }
}

int main() {
    int n;
    cin >> n;
    // cout << get_fibonacci_last_digit_naive(n) << '\n';
    cout << fibonacciLastDigitFast(n) << '\n';
    }

#include<iostream>
using namespace std;

int sumOfNaturalNumbers(int n)
{
    if(n>1)
        return n+sumOfNaturalNumbers(n-1);
    else
        return 1;
}


int main(int argc, char const *argv[])
{
    int x;

    cin >> x;
    cout << sumOfNaturalNumbers(x) << endl;

    return 0;
}

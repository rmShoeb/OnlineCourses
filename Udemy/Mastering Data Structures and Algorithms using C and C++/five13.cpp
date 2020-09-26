#include<iostream>
using namespace std;

void firstFun(int n);
void secondFun(int n);

void firstFun(int n)
{
    if(n>0)
    {
        cout << n << endl;
        secondFun(n-1);
    }
}

void secondFun(int n)
{
    if(n>1)
    {
        cout << n << endl;
        firstFun(n/2);
    }
}

int main(void)
{
    int x;

    cin >> x;
    firstFun(x);

    return 0;
}
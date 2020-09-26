#include<iostream>
using namespace std;

int nCr(int n, int r)
{
    if(r==0||n==r)
        return 1;
    else
        return nCr(n-1, r-1)+nCr(n-1, r);
}

int main(int argc, char const *argv[])
{
    int n;
    int r;

    cin >> n >> r;
    if(r>n)
        cout << "wrong input" << endl;
    else
        cout << nCr(n, r) << endl;

    return 0;
}

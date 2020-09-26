#include<iostream>
using namespace std;

int localFun(int n)
{
    if(n>0) return localFun(n-1)+n;
    return 0;
}

int staticFun(int n)
{
    static int x = 0;
    if(n>0)
    {
        x++;
        return staticFun(n-1)+x;
    }
    return 0;
}


int main(int argc, char const *argv[])
{
    int n;

    cin >> n;
    cout << localFun(n) << endl;
    cout << staticFun(n) << endl;

    return 0;
}

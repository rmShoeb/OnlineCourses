#include<iostream>
using namespace std;

void fun(int n)
{
    if(n>0)
    {
        cout << n << endl;
        fun(n-1);
    }
}

int main(int argc, char const *argv[])
{
    int n;

    cin >> n;
    fun(n);

    return 0;
}

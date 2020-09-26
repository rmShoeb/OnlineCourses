#include<iostream>
using namespace std;

int nestedRecursion(int n)
{
    if(n>100)
    {
        cout << "function: " << n << endl;
        return (n-10);
    }
    else
    {
        cout << "nested: " << n << endl;
        return nestedRecursion(nestedRecursion(n+11));
    }
    
}

int main(int argc, char const *argv[])
{
    int x;

    cin >> x;
    cout << "main: " << nestedRecursion(x) << endl;

    return 0;
}

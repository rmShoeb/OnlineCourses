#include<iostream>
using namespace std;

double taylorSeries(int x, int n)
{
    static double s = 1;

    if(n>0)
    {
        s = 1+(x/(double)n)*s;
        return taylorSeries(x, n-1);
    }
    else
        return s;
}


int main(int argc, char const *argv[])
{
    int x;
    int n;

    cin >> x >> n;
    cout << taylorSeries(x, n) << endl;

    return 0;
}

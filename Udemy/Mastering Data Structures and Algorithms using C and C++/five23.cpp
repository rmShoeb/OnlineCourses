#include<iostream>
#include<cmath>
using namespace std;

// int factorial(int n)
// {
//     if(n>1)
//         return n*factorial(n-1);
//     else
//         return 1;
// }

// double taylorSeries(int x, int n)
// {
//     if(n>0)
//     {
//         return taylorSeries(x,n-1)+(pow(x,n)/(double)factorial(n));
//     }
//     else return 1;
// }


// int main(int argc, char const *argv[])
// {
//     int x;
//     int n;

//     cin >> x >> n;
//     cout << taylorSeries(x, n) << endl;
//     return 0;
// }
double e(int x, int n)
{
    static double p=1,f=1;
    double r;
    if(n==0)
        return 1;
    r=e(x,n-1);
    p=p*x;
    f=f*n;
    return r+p/f;
}
int main()
{
    printf("%lf\n",e(14,25));
}
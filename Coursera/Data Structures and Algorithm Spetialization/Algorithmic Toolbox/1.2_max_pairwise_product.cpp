#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(void)
{
    int iter;
    int temp;
    int numberOfElements;
    int indexOfMax;
    int max = 0;
    vector<int>elemetns;
    
    cin >> numberOfElements;
    for(iter=0; iter<numberOfElements; iter++)
    {
        cin >> temp;
        elemetns.push_back(temp);
        if(max < temp)
        {
            max = temp;
            indexOfMax = iter;
        }
    }
    //elemetns[indexOfMax] = 0;

    temp = 0;
    for(iter=0; iter<numberOfElements; iter++)
    {
        if((temp<elemetns[iter]) && (iter!=indexOfMax))
        {
            temp = elemetns[iter];
        }
    }

    cout << (long long int)max * (long long int)temp;
}

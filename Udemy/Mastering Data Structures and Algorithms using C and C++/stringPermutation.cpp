#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;

char str[100];

void permutationUsingBacktracking(int k)
{
    static char permutatedString[100];
    static int track[100] = {0};
    
    if(str[k] == '\0')
    {
        permutatedString[k] = '\0';
        cout << permutatedString << endl;
    }
    else
    {
        for(int i=0; str[i]!='\0'; i++)
        {
            if(track[i] == 0)
            {
                permutatedString[k] = str[i];
                track[i]++;
                permutationUsingBacktracking(k+1);
                track[i]--;
            }
        }
    }
}


int main(int argc, char const *argv[])
{
    cin >> str;

    permutationUsingBacktracking(0);

    return 0;
}

#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;


bool isAnagram(char sOne[], char sTwo[])
{
    if(strlen(sOne) != strlen(sTwo))
        return false;
    
    int hashTable[26] = {0};
    int iter;

    for(iter=0; sOne[iter]!='\0'; iter++)
    {
        hashTable[sOne[iter]-97]++;
    }

    for(iter=0; sTwo[iter]!='\0'; iter++)
    {
        if(--hashTable[sTwo[iter]-97])
            return false;
    }

    for(iter=0; iter<26; iter++)
    {
        if(hashTable[iter] != 0)
            return false;
    }

    return true;
}


int main(void)
{
    char sOne[100];
    char sTwo[100];

    cin >> sOne >> sTwo;
    
    if(isAnagram(sOne, sTwo))
        cout << "Anagram" << endl;
    else
        cout << "Not Anagram" << endl;
    
    return 0;
}

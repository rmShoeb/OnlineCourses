#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <ctime>
using namespace std;

class HashingChainning
{
private:
	vector<vector<int>> hashTable(10);
public:
	int hash_key(int data){return (data%10);}
	void insert(int data){
		int index = this->hash_key(data);
		this->hashTable[index].push_back(data);
		return;
	}
	bool search(int data){
		int index = this->hash_key(data);
		for(int i=0; i < this->hashTable[index].size(); i++){
			if(this->hashTable[index][i] == data) return true;
		}
		return false;
	}	
};


int main(int argc, char const *argv[])
{
	srand(time(0));

	HashingChainning chain_hash;
	for(int i=0; i<100; i++) chain_hash.insert(rand()%101);
	return 0;
}
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

class LinearProbing
{
private:
	int 	*hashTable;
	bool 	*isThereAnyElement;
	int 	numberOfKeys;
public:
	LinearProbing(){
		LinearProbing(50);
	}
	LinearProbing(int number_of_keys){
		this->numberOfKeys 		= number_of_keys;
		this->hashTable 		= new int[number_of_keys];
		this->isThereAnyElement	= new bool[number_of_keys];
		for(int i=0; i<number_of_keys; i++) isThereAnyElement[i] = false;
	}
	~LinearProbing(){delete []hashTable;}

	int hashKey(int data){return (data%this->numberOfKeys);}
	void insert(int data){
		int i=0;
		int index;
		while(true){
			index = this->hashKey(this->hashKey(data)+i);
			if(!this->isThereAnyElement[index]){
				this->hashTable[index]			= data;
				this->isThereAnyElement[index]	= true;
				break;
			}else i++;
		}
		return;
	}
	bool search(int data){
		cout << data << endl;
		int i=0;
		int index;
		while(true){
			index = this->hashKey(this->hashKey(data)+i);
			if(!this->isThereAnyElement[index]) return false;
			else{
				if(this->hashTable[index] == data) return true;
			}
			i++;
		}
	}
	void printTable(void){
		int index;
		for(index=0; index<this->numberOfKeys; index++){
			if(this->isThereAnyElement[index]) printf("%d\t", this->hashTable[index]);
			else printf("NULL\t");
		}
		printf("\n");
		return;
	}
};


int main(int argc, char const *argv[])
{
	srand(time(0));
	LinearProbing arr(100);
	for(int i=0; i<50; i++){
		arr.insert(rand()%51);
	}
	arr.printTable();
	cout << arr.search(rand()%51) << endl;
	return 0;
}
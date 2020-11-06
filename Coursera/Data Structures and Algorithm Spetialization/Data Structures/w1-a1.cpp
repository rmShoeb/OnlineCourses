#include <iostream>
#include <string>
#include <vector>
using namespace std;

void check_brackets(string text){
	vector<char> stack;
	int iter;
	vector<int> last;

	for(iter=0; iter<text.size(); iter++){
		if(text[iter]=='(' || text[iter]=='{' || text[iter]=='['){
			stack.push_back(text[iter]);
			last.push_back(iter);
		}
		else if(text[iter] == ')'){
			if(stack.empty()){
				cout << iter+1 << endl;
				return;
			}
			else if(stack[stack.size()-1] == '('){
				stack.pop_back();
				last.pop_back();
			}
			else{
				cout << iter+1 << endl;
				return;
			}
		}
		else if(text[iter] == '}'){
			if(stack.empty()){
				cout << iter+1 << endl;
				return;
			}
			else if(stack[stack.size()-1] == '{'){
				stack.pop_back();
				last.pop_back();
			}
			else{
				cout << iter+1 << endl;
				return;
			}
		}
		else if(text[iter] == ']'){
			if(stack.empty()){
				cout << iter+1 << endl;
				return;
			}
			else if(stack[stack.size()-1] == '['){
				stack.pop_back();
				last.pop_back();
			}
			else{
				cout << iter+1 << endl;
				return;
			}
		}
	}
	if(!stack.empty()){
		cout << last[0]+1 << endl;
	}
	else{
		cout << "Success\n";
	}
}

int main(void){
	string input;
	getline(cin, input);
	// cout << input << endl;
	check_brackets(input);

	return 0;
}

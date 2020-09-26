#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;

class BreadthFirstSearch
{
private:
    int         numberOfVertices;
    int         adjacencyMatrix[20][20];
    vector<int> exploring;
    list<int>   visiting;
public:
    BreadthFirstSearch(int number_of_vertices){this->numberOfVertices  = number_of_vertices;}
    void graphInput(void){
        int row, column, input;
        for(row=0; row<this->numberOfVertices; row++){
            for(column=0; column<this->numberOfVertices; column++){
                cin >> adjacencyMatrix[row][column];
            }
        }
    }
    void traverse(int start_node){
        int current_node;
        int column;
        visiting.push_back(start_node);
        while(!visiting.empty() && (exploring.size()!=this->numberOfVertices)){
            //exploring the node
            current_node = visiting.front();
            visiting.pop_front();
            exploring.push_back(current_node);
            for(column=0; column<this->numberOfVertices; column++){
                if(this->adjacencyMatrix[current_node][column]){
                    //checking if there is an edge between current_node and the node column is representing
                    if((find(visiting.begin(),visiting.end(),column)==visiting.end()) && (find(exploring.begin(),exploring.end(),column)==exploring.end())){
                        //conditions
                        //first one is checking if the visiting node is already in visiting queue; if it is, we donot have to add it again in queue
                        //second one is checking if the visiting node is already explored or not
                        visiting.push_back(column);
                    }
                }
            }
        }
        this->printPath();
    }
    void printPath(void){
        for(int i=0; i<this->numberOfVertices; i++){printf("%d ", this->exploring[i]);}
        printf("\n");
    }
};

class DepthFirstSearch
{
private:
    int         numberOfVertices;
    int         adjacencyMatrix[20][20];
    vector<int> exploring;
    vector<int> visiting;
public:
    DepthFirstSearch(int number_of_vertices){this->numberOfVertices  = number_of_vertices;}
    void graphInput(void){
        int row, column, input;
        for(row=0; row<this->numberOfVertices; row++){
            for(column=0; column<this->numberOfVertices; column++){
                cin >> this->adjacencyMatrix[row][column];
            }
        }
    }
    void traverse(int start_node){
        int current_node;
        int column;
        visiting.push_back(start_node);
        while(!visiting.empty() && (exploring.size()!=this->numberOfVertices)){
            //exploring the node
            current_node = visiting[visiting.size()-1];
            visiting.pop_back();
            exploring.push_back(current_node);
            for(column=0; column<this->numberOfVertices; column++){
                if(this->adjacencyMatrix[current_node][column]){
                    //checking if there is an edge between current_node and the node column is representing
                    if((find(visiting.begin(),visiting.end(),column)==visiting.end()) && (find(exploring.begin(),exploring.end(),column)==exploring.end())){
                        //conditions
                        //first one is checking if the visiting node is already in visiting queue; if it is, we donot have to add it again in queue
                        //second one is checking if the visiting node is already explored or not
                        visiting.push_back(column);
                    }
                }
            }
        }
        this->printPath();
    }
    void printPath(void){
        for(int i=0; i<this->numberOfVertices; i++){printf("%d ", this->exploring[i]);}
        printf("\n");
    }
};



int main(void){
    int start_node;
    DepthFirstSearch graph(7);

    graph.graphInput();
    cin >> start_node;
    graph.traverse(start_node);
    return 0;
}
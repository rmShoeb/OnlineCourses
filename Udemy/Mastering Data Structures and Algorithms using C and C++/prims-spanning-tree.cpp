#include <iostream>
#include <cstdint>
#include <cstdbool>
#include <vector>
#define INF INT16_MAX
using namespace std;


bool is_all_node_traversed(bool is_node_selected[], int number_of_vertices){
    for(int i=0; i<number_of_vertices; i++){
        if(!is_node_selected[i]) return false;
    }
    return true;
}

vector<vector<int>> prims_spanning_tree(vector<vector<int>> cost_adjacency_matrix, int number_of_vertices){
    vector<vector<int>> spanning_tree(number_of_vertices);
    bool                is_node_selected[number_of_vertices] = {false};
    int                 row, column;
    int                 spanning_tree_index = 1;
    int                 minimum_cost = INF;
    int                 u, v;
    //select the first edge of minimum cost
    for(row=0; row<number_of_vertices; row++){
        for(column=0; column<=row; column++){
            if(cost_adjacency_matrix[row][column] < minimum_cost){
                minimum_cost    = cost_adjacency_matrix[row][column];
                u               = row;
                v               = column;
            }
        }
    }
    spanning_tree[0].push_back(u);
    spanning_tree[0].push_back(v);
    is_node_selected[u] = is_node_selected[v] = true;
    //generate the spanning tree
    while(!is_all_node_traversed(is_node_selected, number_of_vertices)){
        minimum_cost = INF;
        for(row=0; row<number_of_vertices; row++){
            if(is_node_selected[row]){
                for(column=0; column<number_of_vertices; column++){
                    if((cost_adjacency_matrix[row][column] < minimum_cost) && (!is_node_selected[column])){
                        u               = row;
                        v               = column;
                        minimum_cost    = cost_adjacency_matrix[u][v];
                    }
                }
            }
        }
        spanning_tree[spanning_tree_index].push_back(u);
        spanning_tree[spanning_tree_index].push_back(v);
        spanning_tree_index++;
        is_node_selected[v] = true;
    }

    return spanning_tree;
}

int main(int argc, char const *argv[])
{
    int                 number_of_vertices;
    int                 number_of_edges;
    int                 row, column;

    cin >> number_of_vertices >> number_of_edges;

    vector<vector<int>> cost_adjacency_matrix(number_of_vertices);
    vector<vector<int>> spanning_tree;

    for(row=0; row<number_of_vertices; row++){
        for(column=0; column<number_of_vertices; column++){
            cost_adjacency_matrix[row].push_back(INF);
        }
    }
    for(int i=0; i<number_of_edges; i++){
        cin >> row >> column;
        cin >> cost_adjacency_matrix[row][column];
        cost_adjacency_matrix[column][row] = cost_adjacency_matrix[row][column];
    }
    for(row=0; row<number_of_vertices; row++){
        for(column=0; column<number_of_vertices; column++){
            printf("%12d", cost_adjacency_matrix[row][column]);
        }
        printf("\n");
    }

    spanning_tree = prims_spanning_tree(cost_adjacency_matrix, number_of_vertices);
    for(row=0; row<number_of_vertices-1; row++){
        printf("%3d %3d\n", spanning_tree[row][0], spanning_tree[row][1]);
    }
    printf("\n");

    return 0;
}

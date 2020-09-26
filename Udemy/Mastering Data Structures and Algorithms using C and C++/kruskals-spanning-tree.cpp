#include <iostream>
#include <cstdint>
#include <cstdbool>
#include <vector>
#define INF INT16_MAX
using namespace std;


void join(vector<int>& disjoint_set, int u, int v){
	if(disjoint_set[u] < disjoint_set[v]){
		disjoint_set[u] += disjoint_set[v];
		disjoint_set[v] = u;
	}
	else{
		disjoint_set[v] += disjoint_set[u];
		disjoint_set[u] = v;
	}
}

int find(vector<int>& disjoint_set, int u){
	int x = u;
	while(disjoint_set[x] > 0){
		x = disjoint_set[x];
	}
	return x;
}

bool is_there_cycle(vector<int>& disjoint_set, int u, int v){
	if(find(disjoint_set, u) != find(disjoint_set, v)){
		return false;
	}
	return true;
}

vector<vector<int>> kruskals_spanning_tree(vector<vector<int>>& edges, int number_of_vertices, int number_of_edges){
    vector<vector<int>> spanning_tree(number_of_vertices);
	bool				is_edge_treversed[number_of_edges] = {false};
	vector<int>			disjoint_set(number_of_vertices, -1);
	int					edges_selected=0;
	int					minimum_cost;
	int					minimum_cost_edge;
	int 				u, v;
	int 				i;

	while(edges_selected < number_of_vertices-1){
		minimum_cost = INF;
		//finding the minimum cost edge from the reamining edges
		for(i=0; i<number_of_edges; i++){
			if((!is_edge_treversed[i]) && (edges[i][2]<minimum_cost)){
				u 					= edges[i][0];
				v 					= edges[i][1];
				minimum_cost		= edges[i][2];
				minimum_cost_edge	= i;
			}
		}
		//if the edge meets requirements
		//i.e. does not create loop
		//select the edge
		if(!is_there_cycle(disjoint_set, u, v)){
			//select the edge
			spanning_tree[edges_selected].push_back(u);
			spanning_tree[edges_selected].push_back(v);
			//union of the sets
			join(disjoint_set, find(disjoint_set, u), find(disjoint_set, v));

			edges_selected++;
		}is_edge_treversed[minimum_cost_edge] = true;
	}

    return spanning_tree;
}

int main(int argc, char const *argv[])
{
    int                 number_of_vertices;
    int                 number_of_edges;
    int                 input;

    cin >> number_of_vertices >> number_of_edges;

    vector<vector<int>> edges(number_of_edges);
    vector<vector<int>> spanning_tree;

	for(int i=0; i<number_of_edges; i++){
		//vertex-u
		cin >> input;
		edges[i].push_back(input);
		//vertex-v
		cin >> input;
		edges[i].push_back(input);
		//weight-of-edge
		cin >> input;
		edges[i].push_back(input);
	}
	for(int i=0; i<number_of_edges; i++){
		printf("%3d %3d %3d\n", edges[i][0], edges[i][1], edges[i][2]);
	}

	spanning_tree = kruskals_spanning_tree(edges, number_of_vertices, number_of_edges);
	for(int i=0; i<number_of_vertices-1; i++){
		printf("%3d%3d\n", spanning_tree[i][0], spanning_tree[i][1]);
	}

    return 0;
}

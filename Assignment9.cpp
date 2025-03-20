#include<bits/stdc++.h>
using namespace std;

void dfs(int node,vector<int> &vis, vector<int> adj[],stack<int> &st){
    vis[node] = 1;

    for(auto it : adj[node]){
        if(!vis[it]){
            dfs(it,vis,adj,st);
        }
    }

    st.push(node);
}

void toposort(int n,int m,vector<int> adj[]){

    stack<int> st;
    vector<int> vis(n+1,0);

    for(int i=0;i<n;i++){
        if(!vis[i]){
            dfs(i,vis,adj,st);
        }
    }

    vector<int> ans;
    while(!st.empty()){
        int val = st.top();
        st.pop();

        ans.push_back(val);
    }

    cout <<" Answer array is : " ;
    for(auto it : ans){
        cout<< it <<" ";
    }

    cout << endl;
}

int main(){

    int n,m; cin>>n>>m;

    vector<int> adj[n];
    for(int i=0;i<m;i++){
        int u,v; cin>>u>>v;

        adj[u].push_back(v);
    }

    toposort(n,m,adj);
}

/*
#include<bits/stdc++.h>
using namespace std;

queue <int> que;

int main(){
	int vertex;
	cout<<"Enter the vertex : ";
	cin>>vertex;

	int adj[vertex][vertex];
	int topo[vertex] = {0};
	
	for (int i = 0; i< vertex; i++){
		for (int j = 0; j < vertex; j++){
			adj[i][j] = 0;
                }
        }
	
	char ch = 'y';

        while(ch =='y'){
        	int x, y;
		cout<<"\nEnter the edges : ";
		cin>>x>>y;
		adj[x][y] = 1;
		topo[y] += 1;
		cout<<"Wanna enter more edges?(y/n) : ";
		cin>>ch; 
        }

	for (int i = 0; i < vertex; i++){
		if (topo[i] == 0){
			que.push(i);
			topo[i] = -1;
		}
	}

	if(que.empty()){
		cout<<"\nNot an acyclic directed graph!!";
	}

	cout<<"topological Sort: ";
	while(!que.empty()){
		int x = que.front();
		for (int i = 0; i < vertex; i++){
			if (adj[x][i] == 1){
				topo[i] -= 1;
				if (topo[i] == 0){
					topo[i] = -1;
					que.push(i);
				}
			}
		}
		cout<<" "<<x;
		que.pop();
	}
}

*/
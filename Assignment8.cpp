#include<bits/stdc++.h>
using namespace std;

void dijktra(int start,int end,vector<vector<pair<int,int>>> &adj, int n, int m){
    
    vector<int> dist(n+1,1e9);
    priority_queue<pair<int,int>,vector<pair<int,int>> , greater<pair<int,int>> > pq;
    // distance node
    dist[start] = 0;
    pq.push({0,start});

    while(!pq.empty()){
        auto it = pq.top();
        pq.pop();

        int dis = it.first;
        int node = it.second;

        for(auto itr : adj[node]){
            int adjnode = itr.first;
            int edW = itr.second;

            if(edW + dis < dist[adjnode]){
                dist[adjnode] = edW + dis;
                pq.push({edW+dis,adjnode});
            }
        }
    }

    if(dist[end] == 1e9) cout <<"Not possible to reach " << end <<" from " << start << endl;
    else cout <<"Minimum distance to reach "<< end <<" from " << start << " is " << dist[end] << endl;

}

int main(){
    // implement dijkstra's

    int n; cin>>n; // number of cities
    int m; cin>>m; // number of routes

    vector<vector<pair<int,int>>> adj(n+1);

    for(int i=0;i<m;i++){
        int u,v,w;
        cin>>u>>v>>w;

        adj[u].push_back({v,w});
        adj[v].push_back({u,w});
    }

    cout <<"----------"<<endl;
    int start,end;
    cin>>start>>end;

    cout << "----------" << endl;
    dijktra(start,end,adj,n,m);
    cout << "----------" << endl;
}

/*

5 5
1 2 6
1 3 7
2 3 2
3 4 4
4 5 5
1 5

*/
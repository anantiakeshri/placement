#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int dijikstra(long long int start,vector<vector<long long int>> adj,vector<long long int> special,long long int N){
    
    queue<long long int> q;
    vector< long long int> dist(N + 1, INT_MAX);
 
    // pq.push({0, start});
    q.push(start);
    dist[start] = 0;
 
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (long long int i = 0;i<adj[u].size();i++) {
            long long int v = adj[u][i]; // adj vertes
 
            // If there is shorted path to v through u.
            if (dist[v] > dist[u] + 1) {
                // Updating distance of v
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    long long int ANS = INT_MAX;
    for(long long int i = 0;i<special.size();i++){
        ANS = min(dist[special[i]],ANS);
    }
    return (ANS == INT_MAX)? -1:ANS;
}

int main() {
	long long int T;
	cin>>T;
	while(T--){
	    long long int N , M , K;
	    cin>>N>>M>>K;
	    vector<vector<long long int>> adj(N + 1,vector<long long int>(0,0));
	    vector<long long int>special(0,0);
	    for(long long int i = 0;i<M;i++){ // graph
	        long long int u , v;
	        cin>>u>>v;
	        adj[u].push_back(v);
	        adj[v].push_back(u);
	    }
	    for(long long int i = 0;i<K;i++){ // special nodes
	        long long int temp;
	        cin>>temp;
	        special.push_back(temp);
	    }
	    long long int Q;
	    cin>>Q;
	    while(Q--){
	        long long int start;
	        cin>>start;
	        // we apply dijikstra to find nearest of portal
	        cout<<dijikstra(start,adj,special,N)<<endl;
	        
	    }
	}
	return 0;
}

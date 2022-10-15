//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int shortestPath(vector<vector<int>> &grid, pair<int, int> s,pair<int, int> d) {

    queue<pair<int,int> > q;

    int dx[]={-1,1,0,0};

    int dy[]={0,0,-1,1};

    q.push(s);

    q.push({-1,-1});

    int ans=0;

    while (!q.empty())

    {

        pair<int,int> curr=q.front();

        q.pop();

        if(curr.first==-1 && curr.second==-1){

            if(!q.empty()){

                q.push({-1,-1});

 

            }

            ans++;

            

        }

        else if(curr==d){

            return ans;

        }

        else

        {

            for (int i = 0; i < 4; i++)

            {

                if(curr.first+dx[i]>=0 && curr.first+dx[i]<grid.size() && curr.second+dy[i]>=0 && curr.second+dy[i]<grid[0].size()  && grid[curr.first+dx[i]][curr.second+dy[i]]==1){

                    grid[curr.first+dx[i]][curr.second+dy[i]]=0;

                    q.push({(curr.first)+dx[i],(curr.second)+dy[i]});

 

                }

                /* code */

            }

            

        }

        

        

        

        /* code */

    }

 

 

    return -1;

 

}
};


//{ Driver Code Starts.
int main() {

    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> grid(n, vector<int>(m));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }

        pair<int, int> source, destination;
        cin >> source.first >> source.second;
        cin >> destination.first >> destination.second;
        Solution obj;
        cout << obj.shortestPath(grid, source, destination) << endl;
    }
}

// } Driver Code Ends
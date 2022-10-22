//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution {
  public:
    int mod = 1e8;
    int fillingBucket(int N) 
    {
        int prev1 = 1;
        int prev2 = 1;
        
        for(int i = 2; i <= N; i++) {
            int ans = (prev1 + prev2) % mod;
            prev2 = prev1;
            prev1 = ans;
        }
        
        return prev1;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        
        cin>>N;

        Solution ob;
        cout << ob.fillingBucket(N) << endl;
    }
    return 0;
}
// } Driver Code Ends
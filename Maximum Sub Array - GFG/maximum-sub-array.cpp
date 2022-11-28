//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
//User function template for C++
class Solution{
public:
	vector<int> findSubarray(int a[], int n) {
	    // code here
	    int start=0;
	    int end=-1;
	    int sum=0;
	    int maxi=0;
	    int i=0;
	    int j=0;
	    int diff=0;
	    while(j<n)
	    {
	        if(a[j]>=0)
	        {
	            sum+=a[j];
	            j++;
	        }
	        else {
	            if((maxi==sum && diff<j-i-1 )||(maxi<sum))
	            {
	                maxi=sum;
	                start=i;
	                end=j-1;
	                 diff=end-start;
	                 
	            }
	            sum=0;
	            i=j;
	            j++;
	            i++;
	            
	        }
	    }
	     if((maxi==sum && diff<j-i-1)||(maxi<sum))
	            {
	                maxi=sum;
	                start=i;
	                end=j-1;
	                 diff=end-start;
	                 
	            }
	            
	            vector<int>v;
	            for(int i=start;i<=end;i++)
	              v.push_back(a[i]);
	              
	              if(v.size()==0)
	              v.push_back(-1);
	              return v;
	}
};

//{ Driver Code Starts.

void printAns(vector<int> &ans) {
    for (auto &x : ans) {
        cout << x << " ";
    }
    cout << "\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, i;
        cin >> n;
        int a[n];
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.findSubarray(a, n);
        printAns(ans);
    }
    return 0;
}

// } Driver Code Ends
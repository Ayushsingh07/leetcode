//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

#define ll long long


// } Driver Code Ends
//User function template for C++
class Solution{
public:
	// #define ll long long

	 ll countSubarray(int arr[], int n, int k) {

     int f=-1; // index of element > k seen till now

     long long c=0;

     for(int i=0;i<n;i++){

         if(arr[i]>k){

             c=c+(n-i)*(i-f); // calculate the subarrays

             f=i; // updating the index

         }

     }

     return c;

 }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k, i;
        cin >> n >> k;
        int arr[n];
        for (i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.countSubarray(arr, n, k);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends
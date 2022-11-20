//{ Driver Code Starts
// Initial Template for C++

// Initial Template for C++
// Back-end complete function Template for C++
// User function Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {

  public:

  

    bool isCoprime(int x1, int x2) {

        

        //TC = O(log(max(x1, x2)))

        if(__gcd(x1, x2) == 1) return true;

        else return false;

    }

    long long lcmTriplets(long long n) {

        //case1 when n is less than 3

        if(n == 1) return 1;

        if(n == 2) return 2;

        

        //case 2 when n is odd ans = n*n-1*n-2;

        if(n%2 == 1) {

            long long ans = n*(n-1)*1LL;

            return ans*(n-2);

        }

        

        //case 3 when n is even but not divisible by 3

        if(n%2 == 0 && n%3 != 0) {

            long long ans = n*(n-1)*1LL;

            return ans*(n-3);

        }

        

        //case 4 if n is even and also div by 3

        //eg n = 6

        int x1 = n, x2 = n-1, x3 = n-2;

        while(min(x1, min(x2, x3)) > 0) {

            int mn = min(x1, min(x2, x3));

            int mx = max(x1, max(x2, x3));

            if(mx-mn <= 3) {

                if(isCoprime(x1, x2) && isCoprime(x2, x3) && isCoprime(x3, x1)) {

                    long ans = x1*x2*1LL;

                    return ans*x3; 

                }

                x3 = x3-1;

            } else {

                x3 = x3+1;

                x2 = x2-1;

                x1 = x1-1;

                long ans = x1*x2*1LL;

                return ans*x3; 

            }

        } 

        return -1;

    }

};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long N;
        cin >> N;
        Solution ob;
        cout << ob.lcmTriplets(N) << "\n";
    }
}
// } Driver Code Ends
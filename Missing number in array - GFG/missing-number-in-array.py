#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        
        sum_=n*(n+1)/2
        for i in array:
            sum_-=i
       
        return int(sum_)

#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends
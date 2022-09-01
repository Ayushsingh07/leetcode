class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_=prices[0]
        max_=0
        for i in range(len(prices)-1):
            if prices[i]<min_:
                
                min_=prices[i]
            if max_<(prices[i+1]-min_):
                max_=prices[i+1]-min_
            #print(max,prices[i])
        return max_
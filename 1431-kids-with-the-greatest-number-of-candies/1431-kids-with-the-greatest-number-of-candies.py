class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out=[]
        m= max(candies)
        
        for i in range(0,len(candies)):
            
            if candies[i]+extraCandies>=m :
              out.append(True)
                
            else:
                out.append(False)
        return out
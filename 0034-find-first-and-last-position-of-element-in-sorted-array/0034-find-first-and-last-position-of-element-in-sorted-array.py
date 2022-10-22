class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        if n==0 or target not in nums:
            return [-1,-1]
        l=0
        h=n-1
        a=[]
        ans=0
    
        while l<=h:
            m=(l+h)>>1
            if nums[m]==target:
                ans=m
                h=m-1
            elif nums[m]>target:
                h=m-1
            else:
                l=m+1
  
        a.append(ans)
        l=ans
        h=n-1
        while l<=h:
            m=(l+h)>>1
            if nums[m]==target:
                ans=m
                l=m+1
            elif nums[m]<target:
                l=m+1
                
            else:
                h=m-1
        a.append(ans)
        return a
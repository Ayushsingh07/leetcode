class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=0
        
        high=len(nums)-1
        
        while low<high:
            
            m=(low+high)//2
            
            if nums[m]>nums[m+1]:
                
                high=m
            else:
                low=m+1
        return low
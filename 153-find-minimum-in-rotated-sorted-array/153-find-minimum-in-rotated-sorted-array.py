class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]
        if nums[0]<nums[len(nums)-1]:
            return nums[0]
        
        low=0
        high=len(nums)-1
        
        while low<=high:
            mid=(low+high)//2
            
            #res=nums[mid]
            
            if nums[low]<nums[high]:
                res=min(res,nums[low])
                break
            res=min(res,nums[mid])
            if nums[mid]>=nums[low]:
                low=mid+1
            else:
                high=mid-1
        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r=[]
        nums.sort()
        
        for i in range(len(nums)):
            
            l=i+1
            h=len(nums)-1
            
            while l<h:
                
                if nums[i]+nums[l]+nums[h]==0:
                    r.append((nums[i],nums[l],nums[h]))
                    
                    h-=1
                    l+=1
                
                elif nums[i]+nums[l]+nums[h]>0:
                    h-=1
                else:
                    l+=1
        return set(r)
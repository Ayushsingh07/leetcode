class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        l=[]
        for i in range(len(nums)):
            val=target-nums[i]
    
            key=list(dic.keys())
   
    
            if nums[i] in key :
                l.append(i)
                l.append(dic.get(nums[i]))
        
            else:
                dic[val]=i
        return l
        
        
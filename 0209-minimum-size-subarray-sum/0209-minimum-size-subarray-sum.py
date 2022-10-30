from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        startIndex = 0
        endIndex = 0
        currentSubArrayLength = float("inf")
        currentSum = 0
        
        while endIndex < len(nums):
            currentSum += nums[endIndex]
            
            while startIndex <= endIndex and currentSum >= target:
                currentSubArrayLength = min(currentSubArrayLength, endIndex-startIndex+1)
                currentSum -= nums[startIndex]
                startIndex += 1
                
            endIndex += 1
            
        return 0 if currentSubArrayLength ==  float("inf") else currentSubArrayLength
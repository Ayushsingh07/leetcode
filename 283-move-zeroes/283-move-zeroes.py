class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        n=0
        for i in range(l):
            if nums[i] !=0:
                nums[n]=nums[i]
                n+=1
        for i in range(n,l):
            nums[i]=0
            
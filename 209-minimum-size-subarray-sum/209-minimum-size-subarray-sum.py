class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        ind = 0
        res = 10 ** 9
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                res = min(res, i - ind + 1)
                s -= nums[ind]
                ind += 1
        return res if res != 10 ** 9 else 0
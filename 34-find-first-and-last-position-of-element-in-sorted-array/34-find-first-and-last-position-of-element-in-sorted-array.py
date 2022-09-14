class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:

		def binSearch(nums, target, isLeft = True, initLo = 0):
			lo,hi = initLo,len(nums)-1

			while lo < hi:
				mid = (lo+hi)>>1 if isLeft else ((lo+hi)>>1)+1

				if nums[mid] < target:
					lo = mid + 1 if isLeft else mid
				elif nums[mid] > target:
					hi = mid if isLeft else mid-1
				else:
					if isLeft:
						hi = mid
					else:
						lo = mid
			return lo if nums[lo] == target else -1


		if len(nums) == 0:
			return [-1,-1]


		res = [binSearch(nums, target),-1]
		res[1] = -1 if res[0] == -1 else binSearch(nums, target, False, res[0])
		return res